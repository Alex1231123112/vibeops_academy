"""Админка для публикации постов в Telegram-канал."""
from __future__ import annotations

import asyncio
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config import ADMIN_PASSWORD, BOT_TOKEN, CHANNEL_ID
from telegram_client import send_message, send_photo

app = FastAPI(title="VibeOps Telegram Admin")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

SCHEDULE_FILE = BASE_DIR / "scheduled.json"
SENT_POSTS_FILE = BASE_DIR / "sent_posts.json"
MOSCOW_TZ = timezone(timedelta(hours=3))
MAX_SENT_IN_LIST = 100


def check_auth(password: str | None = None) -> bool:
    """Проверка пароля (если задан ADMIN_PASSWORD)."""
    if not ADMIN_PASSWORD:
        return True
    return password == ADMIN_PASSWORD


def load_scheduled() -> list[dict[str, Any]]:
    if not SCHEDULE_FILE.exists():
        return []
    try:
        return json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_scheduled(items: list[dict[str, Any]]) -> None:
    SCHEDULE_FILE.write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_sent_posts() -> list[dict[str, Any]]:
    if not SENT_POSTS_FILE.exists():
        return []
    try:
        return json.loads(SENT_POSTS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def append_sent_post(text: str, photo_url: str = "") -> None:
    now_utc = datetime.now(timezone.utc)
    items = load_sent_posts()
    items.insert(
        0,
        {
            "text": text,
            "photo_url": photo_url,
            "sent_at": now_utc.isoformat(),
        },
    )
    # Храним только последние MAX_SENT_IN_LIST
    items = items[:MAX_SENT_IN_LIST]
    SENT_POSTS_FILE.write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def parse_scheduled_at(raw: str) -> datetime | None:
    """Парсинг даты/времени из <input type=\"datetime-local\"> в UTC."""
    raw = raw.strip()
    if not raw:
        return None
    try:
        # Формат вида 2026-03-11T10:30
        local_dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if local_dt.tzinfo is None:
        local_dt = local_dt.replace(tzinfo=MOSCOW_TZ)
    return local_dt.astimezone(timezone.utc)


async def process_due_posts() -> None:
    """Отправка всех постов, у которых наступило время публикации."""
    items = load_scheduled()
    if not items:
        return

    now_utc = datetime.now(timezone.utc)
    remaining: list[dict[str, Any]] = []

    for item in items:
        scheduled_at_raw = item.get("scheduled_at")
        if not scheduled_at_raw:
            continue
        try:
            scheduled_at = datetime.fromisoformat(scheduled_at_raw)
        except ValueError:
            # Повреждённая запись — пропускаем
            continue

        if scheduled_at > now_utc:
            remaining.append(item)
            continue

        text = item.get("text", "")
        photo_url = (item.get("photo_url") or "").strip()

        try:
            if photo_url:
                await send_photo(caption=text, photo_url=photo_url)
            else:
                await send_message(text=text)
            append_sent_post(text, photo_url)
        except httpx.HTTPError:
            # Если отправка упала — оставим запись, попробуем позже
            remaining.append(item)

    if len(remaining) != len(items):
        save_scheduled(remaining)


async def scheduler_loop() -> None:
    """Фоновый цикл проверки отложенных постов."""
    while True:
        await process_due_posts()
        await asyncio.sleep(30)


@app.on_event("startup")
async def on_startup() -> None:
    # Стартуем фоновый планировщик
    asyncio.create_task(scheduler_loop())


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Главная страница — форма создания поста + список отложенных."""
    scheduled_raw = load_scheduled()

    # Для отображения конвертируем время в московское
    scheduled_for_view: list[dict[str, Any]] = []
    for item in scheduled_raw:
        iso = item.get("scheduled_at")
        if not iso:
            continue
        try:
            dt_utc = datetime.fromisoformat(iso)
            dt_local = dt_utc.astimezone(MOSCOW_TZ)
            display_time = dt_local.strftime("%d.%m.%Y %H:%M")
        except ValueError:
            display_time = iso
        scheduled_for_view.append(
            {
                "text": item.get("text", "")[:80],
                "photo_url": item.get("photo_url") or "",
                "scheduled_at": display_time,
            }
        )

    # Опубликованные посты (новые сверху)
    sent_raw = load_sent_posts()
    sent_for_view: list[dict[str, Any]] = []
    for item in sent_raw[:MAX_SENT_IN_LIST]:
        iso = item.get("sent_at")
        if not iso:
            continue
        try:
            dt_utc = datetime.fromisoformat(iso)
            dt_local = dt_utc.astimezone(MOSCOW_TZ)
            display_time = dt_local.strftime("%d.%m.%Y %H:%M")
        except ValueError:
            display_time = iso
        raw_text = item.get("text", "")
        text_preview = raw_text[:200] + ("…" if len(raw_text) > 200 else "")
        sent_for_view.append(
            {
                "text": text_preview,
                "photo_url": item.get("photo_url") or "",
                "sent_at": display_time,
            }
        )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "channel_id": CHANNEL_ID,
            "scheduled_posts": scheduled_for_view,
            "sent_posts": sent_for_view,
        },
    )


@app.post("/publish")
async def publish(
    request: Request,
    text: str = Form(...),
    password: str = Form(""),
    photo_url: str = Form(""),
    scheduled_at: str = Form(""),
):
    """Опубликовать пост в канал или отложить публикацию."""
    if not check_auth(password):
        raise HTTPException(status_code=401, detail="Неверный пароль")

    if not BOT_TOKEN:
        raise HTTPException(
            status_code=500,
            detail="BOT_TOKEN не настроен. Добавьте в .env",
        )

    # Если указано время в будущем — сохраняем как отложенный пост
    dt_utc = parse_scheduled_at(scheduled_at)
    now_utc = datetime.now(timezone.utc)
    if dt_utc and dt_utc > now_utc + timedelta(seconds=10):
        items = load_scheduled()
        items.append(
            {
                "text": text,
                "photo_url": photo_url.strip(),
                "scheduled_at": dt_utc.isoformat(),
                "created_at": now_utc.isoformat(),
            }
        )
        save_scheduled(items)
        return RedirectResponse(url="/?scheduled=1", status_code=303)

    # Иначе — отправляем сразу
    try:
        if photo_url.strip():
            result = await send_photo(caption=text, photo_url=photo_url.strip())
        else:
            result = await send_message(text=text)

        if not result.get("ok"):
            raise HTTPException(
                status_code=400,
                detail=result.get("description", "Ошибка Telegram API"),
            )
        append_sent_post(text, photo_url.strip())
        return RedirectResponse(url="/?success=1", status_code=303)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    """Проверка работы сервиса."""
    return {"status": "ok", "channel": CHANNEL_ID}

"""Клиент Telegram Bot API."""
import httpx
from config import BOT_TOKEN, CHANNEL_ID


async def send_message(text: str, parse_mode: str = "HTML") -> dict:
    """Отправить сообщение в канал."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()


async def send_photo(caption: str, photo_url: str, parse_mode: str = "HTML") -> dict:
    """Отправить фото с подписью в канал."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": photo_url,
        "caption": caption,
        "parse_mode": parse_mode,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()

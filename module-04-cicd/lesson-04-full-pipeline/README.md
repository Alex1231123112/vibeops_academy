# Урок 4.4: Полный пайплайн

## 🎯 Цели урока
- От push до продакшна
- Тесты → Сборка → Деплой
- Мониторинг и логи

## ⏱️ Сколько времени

Ориентир: **3–6 часов** (собрать CI+CD+health+logs+secrets).

## 📺 Видео

- [Все видео курса](../../resources/videos.md)

## Что такое “полный пайплайн” в учебном проде

Минимально приемлемый pipeline для junior-ready проекта:

1) **CI**: на `push` и `pull_request` — тесты.  
2) **CD**: на `push` в `main` — деплой.  
3) **Прод-минимум**: health endpoint, логи, секреты из окружения.

## 1) CI: тесты на каждый push/PR

Минимальный workflow `Test`:

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"
      - run: pip install -r requirements.txt
      - run: pytest
```

## 2) CD: деплой на main

Подход зависит от платформы. Самый простой учебный вариант — “deploy hook” (Render) или CLI/API провайдера.

Важно: **секреты** (токены, ключи, hook URL) — только в GitHub Secrets.

## 3) Секреты и конфиги

### Где хранить

- локально: `.env` (не коммитить)
- в CI/CD: GitHub Secrets
- в проде: переменные окружения платформы (Render/Railway)

### Что не должно попасть в Git

- `.env`, ключи, токены, приватные URL

## 4) Health endpoint

Минимальный `/health`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

Зачем:
- платформа/балансер понимают, что сервис жив;
- вы понимаете, что деплой успешен.

## 5) Логи

Минимальный логгер:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger("app")
log.info("service_started")
```

Что логировать:
- старт приложения
- ключевые действия (например обработка запроса)
- ошибки с контекстом (но без секретов)

## ✅ Чек-лист полного пайплайна

- [ ] Есть CI workflow: tests на push/PR
- [ ] Есть CD workflow: deploy на main
- [ ] Секреты в GitHub Secrets (не в коде)
- [ ] Есть `/health` и вы проверяете его после деплоя
- [ ] Есть базовые логи, по которым можно понять "что происходит"

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

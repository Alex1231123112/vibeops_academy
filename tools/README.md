# Инструменты VibeOps

## Админки для Telegram-канала

### 1. Простая админка (telegram-admin)

Одна форма для быстрой публикации поста. Без БД, без авторизации (опционально пароль).

- [telegram-admin/README.md](telegram-admin/README.md) — настройка и запуск
- Порт: **8800**
- Запуск из корня: `docker compose up -d` (после создания `.env`)

### 2. Полная админка (HT)

Контент-план, рассылки, аналитика. React + FastAPI + PostgreSQL.

- [ht-admin-vibeops/README.md](ht-admin-vibeops/README.md) — установка HT и настройка для VibeOps
- Порт: **8800** (frontend)
- Требует клонирования [HT](https://github.com/Alex1231123112/HT)

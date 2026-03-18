# Админка на базе HT

Полнофункциональная админ-панель для Telegram-канала VibeOps на базе проекта [HT](https://github.com/Alex1231123112/HT).

## Возможности HT

- **Контент-план** — создание, планирование, отправка постов
- **Рассылки** — в бот и/или канал
- **Аналитика** — метрики и логи
- **JWT-авторизация** — безопасный вход
- **React + FastAPI** — современный стек

## Установка

### 1. Клонируйте HT

```bash
cd tools
git clone https://github.com/Alex1231123112/HT.git ht-admin
cd ht-admin
```

Или как submodule:

```bash
git submodule add https://github.com/Alex1231123112/HT.git tools/ht-admin
cd tools/ht-admin
```

### 2. Настройте окружение

```bash
cp ../ht-admin-vibeops/.env.vibeops.example .env
# Отредактируйте .env: BOT_TOKEN, JWT_SECRET, ADMIN_DEFAULT_PASSWORD
```

### 3. Запуск (порт 8800)

```bash
docker compose -f docker-compose.yml -f ../ht-admin-vibeops/docker-compose.vibeops.yml up -d --build
```

Админка: **http://localhost:8800**

### 4. Настройка канала VibeOps

1. Войдите в админку (admin / пароль из ADMIN_DEFAULT_PASSWORD)
2. Создайте канал рассылки: тип «Telegram-канал», @vibeops_academy
3. Добавьте бота в канал как администратора с правом публикации
4. Создайте контент-план → привяжите канал → «Отправить»

## Порты

| Сервис | Порт |
|--------|------|
| Frontend (админка) | 8800 |
| API | 8000 |
| PostgreSQL | 5433 |
| MinIO | 9000, 9001 |

## Документация HT

- [HT README](https://github.com/Alex1231123112/HT)
- [Руководство администратора](https://github.com/Alex1231123112/HT/blob/main/docs/ADMIN_GUIDE.md)

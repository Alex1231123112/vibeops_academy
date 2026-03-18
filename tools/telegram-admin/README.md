# Админка для Telegram-канала VibeOps

Веб-интерфейс для создания и публикации постов в Telegram-канал курса.

## Настройка

### 1. Создайте бота

1. Напишите [@BotFather](https://t.me/BotFather) в Telegram
2. Команда `/newbot` → придумайте имя
3. Сохраните **Bot Token**

### 2. Добавьте бота в канал

1. Откройте канал → Управление → Администраторы
2. Добавьте бота как администратора с правом публикации

### 3. Узнайте ID канала

- Для публичного канала: `@vibeops_academy` (username с @)
- Для приватного: используйте бота [@userinfobot](https://t.me/userinfobot) или API `getUpdates`

### 4. Запуск

**Вариант A: Docker (из корня курса)**

```bash
cd vibeops_academy
cp tools/telegram-admin/.env.example tools/telegram-admin/.env
# Отредактируйте tools/telegram-admin/.env: BOT_TOKEN, CHANNEL_ID

docker compose up -d
```

Откройте http://localhost:8800

**Вариант B: Локально**

```bash
cd tools/telegram-admin
cp .env.example .env
# Отредактируйте .env: BOT_TOKEN, CHANNEL_ID

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8800
```

Откройте http://localhost:8800

## Безопасность

- `.env` не коммитить в Git
- Добавьте `ADMIN_PASSWORD` в .env для защиты формы
- Используйте только на localhost или за reverse proxy с HTTPS

## Отложенные посты

В форме есть поле **«Отправить позже (по Москве)»**.

- если поле пустое — пост отправится сразу;
- если указать дату/время в будущем — пост сохранится в очередь и отправится автоматически.

Отложенные посты хранятся в файле `scheduled.json` рядом с `main.py` (внутри контейнера или локальной папки) и отображаются списком под формой.

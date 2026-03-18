# Урок 3.3: Docker Compose

## 🎯 Цели урока
- docker-compose.yml
- Несколько сервисов (app + db)
- Запуск и остановка

## ⏱️ Сколько времени

Ориентир: **2–3 часа** (собрать compose + проверить работу).

## 📺 Видео

- [Все видео курса](../../resources/videos.md)

## 📖 Теория (минимум)

Docker Compose — это способ описать несколько контейнеров в одном файле и запускать их одной командой.

### Минимум понятий

- `services` — контейнеры (app, db, cache и т.п.)
- `build` — как собрать образ приложения
- `image` — готовый образ (например Postgres)
- `ports` — проброс портов
- `environment` — переменные окружения
- `volumes` — данные, которые нужно сохранять между перезапусками

## 📁 Примеры compose

См. `examples/`:

- [docker-compose.yml](examples/docker-compose.yml) — один сервис
- [docker-compose.with-db.yml](examples/docker-compose.with-db.yml) — app + postgres + volume

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## ✅ Чек-лист

- [ ] Я понимаю, что такое `services` и как они общаются по имени (например `db`)
- [ ] Я умею поднять и остановить сервисы одной командой
- [ ] Я понимаю, зачем нужны `volumes`

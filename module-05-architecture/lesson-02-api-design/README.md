# Урок 5.2: Дизайн API

## 🎯 Цели урока
- REST API основы
- OpenAPI спецификация
- Микросервисы vs монолит

## ⏱️ Сколько времени

Ориентир: **2–4 часа** (описать контракт API + придумать edge cases).

## 📺 Видео

- [Все видео курса](../../resources/videos.md)

## 📖 Теория (минимум)

### Контракт важнее реализации

Для API важно заранее определить:
- эндпоинты и методы (`GET /health`, `POST /items`)
- формат запросов/ответов (JSON поля)
- ошибки (коды 400/404/500 и что в теле)

### REST (очень кратко)

- Ресурсы: `/items`, `/users`
- Методы: GET/POST/PATCH/DELETE
- Статусы: 200/201/204/400/401/404

### OpenAPI

OpenAPI — описание API в YAML/JSON, которое можно использовать для документации и проверки.

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## ✅ Чек-лист

- [ ] Я могу описать API как контракт (эндпоинты + форматы + ошибки)
- [ ] У меня есть минимум 3 edge cases и как API должен отвечать
- [ ] Я понимаю, когда уместен монолит, а когда микросервисы

## 🤖 AI-агент

Для проектирования API используйте [Backend Architect](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-backend-architect.md) из agency-agents.

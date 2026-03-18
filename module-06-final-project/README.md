# Модуль 6: Финальный проект

Соберите полноценное приложение от идеи до продакшна.

## 🎯 Цель модуля

Собрать проект “junior-ready”, в котором есть:
- код и история изменений в GitHub,
- воспроизводимый запуск (Docker/Docker Compose),
- CI (тесты) и CD (деплой),
- прод-минимум: `/health`, логи, secrets, HTTPS.

## ⏱️ Сколько времени

Ориентир: **6–12 часов** (можно растянуть на 1–2 недели).

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание (что сдавать)

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md) (и [project-template/prompts.md](project-template/prompts.md)).

## ✅ Артефакты по модулю (что должно получиться)

- Репозиторий на GitHub + понятный README
- Работающий деплой по HTTPS
- `/health` endpoint
- Базовые логи
- `Dockerfile`, `docker-compose.yml`, `.dockerignore`, запуск не под root (`USER`)
- GitHub Actions: тесты на `push/pull_request` + деплой на `main`
- Базовые тесты (pytest или аналог)

## Ресурсы

- [Идеи для проектов](project-ideas.md)
- [Шаблон проекта](project-template/)
- [Примеры работ](examples/)

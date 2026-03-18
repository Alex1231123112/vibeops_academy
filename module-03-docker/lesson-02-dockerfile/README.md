# Урок 3.2: Dockerfile

## 🎯 Цели урока
- Синтаксис Dockerfile
- FROM, COPY, RUN, CMD
- Создание образа для Python-приложения

## ⏱️ Сколько времени

Ориентир: **2–3 часа** (собрать образ под свой проект).

## 📺 Видео
- [Docker 2025: Полный Курс с ПРАКТИКОЙ За 1 Час](https://www.youtube.com/watch?v=-yq-HVZIFEQ)
- [Docker — Полный курс для начинающих](https://www.youtube.com/watch?v=_uZQtRyF6Eg) (3 ч)
- [Все видео курса](../../resources/videos.md)

## 📖 Теория (минимум)

### Типовой “скелет” Dockerfile

- `FROM` — базовый образ
- `WORKDIR` — рабочая директория
- `COPY` — копирование файлов в образ
- `RUN` — команды на этапе сборки (установка зависимостей)
- `CMD` — команда запуска контейнера

## 📁 Примеры Dockerfile

См. папку `examples/`:

- [Dockerfile.simple](examples/Dockerfile.simple) — простой Python-образ
- [Dockerfile.python](examples/Dockerfile.python) — multi-stage вариант
- [Dockerfile.node](examples/Dockerfile.node) — пример для Node.js

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## ✅ Чек-лист

- [ ] Я понимаю, что делается на этапе build (RUN) и на этапе run (CMD)
- [ ] Я умею собрать образ и запустить его
- [ ] У меня есть Dockerfile для своего проекта

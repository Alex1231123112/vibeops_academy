# Урок 4.2: GitHub Actions

## 🎯 Цели урока
- Workflow файлы
- Триггеры: push, pull_request
- Деплой на Render/Railway

## ⏱️ Сколько времени

Ориентир: **2–4 часа** (сделать CI workflow + (желательно) deploy workflow).

## 📺 Видео
- [Пишем реальный CI/CD пайплайн \| GITLAB CI/CD](https://www.youtube.com/watch?v=prOarIqL5Qs) (19 мин)
- [Полный Курс по GitHub Actions](https://genius.courses/) (5 ч)
- [Все видео курса](../../resources/videos.md)

## 📖 Теория (минимум)

### Что такое workflow

Workflow — это YAML файл в `.github/workflows/*.yml`, который GitHub запускает по событиям (`push`, `pull_request`).

Минимальный CI обычно делает:
- checkout кода
- установка runtime (Python)
- установка зависимостей
- запуск тестов/линтера

## 📁 Примеры workflow

См. `examples/`:
- `simple.yml` — самый простой workflow
- `test.yml` — пример под pytest
- `deploy.yml` — заготовка под deploy job

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## ✅ Чек-лист

- [ ] У меня есть CI на `push` и `pull_request`
- [ ] Я знаю, где смотреть логи workflow
- [ ] Секреты не в коде, а в GitHub Secrets

## 🤖 AI-агент

Для проектирования пайплайнов используйте [DevOps Automator](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-devops-automator.md) из [agency-agents](https://github.com/msitarzewski/agency-agents).

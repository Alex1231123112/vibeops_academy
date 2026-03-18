# Урок 2.3: Настройка Cursor

## 🎯 Цели урока
- Установка Cursor
- Базовые горячие клавиши
- Интеграция с проектом
- Специализированные AI-агенты (agency-agents)

## ⏱️ Сколько времени

Ориентир: **1–2 часа** (установка + настройка под проект).

## 📺 Видео

- [480 часов с Cursor: как я упростил себе кодинг с AI](https://www.youtube.com/watch?v=uDJUwls-Gpw) (25 мин)
- [Cursor AI на максималках! 7 фичей](https://www.youtube.com/watch?v=pHr179iQ6rU) (18 мин)
- [Все видео курса](../../resources/videos.md)

## 📖 Теория (минимум)

### Базовые горячие клавиши
- `Ctrl+K` — inline-редактирование с AI
- `Ctrl+L` — открыть чат
- `Ctrl+` ` — терминал

### Специализированные агенты

Вместо generic-промптов используйте [agency-agents](https://github.com/msitarzewski/agency-agents) — коллекцию из 100+ AI-агентов с экспертизой в разных областях.

**Релевантные для курса:**
- **DevOps Automator** — CI/CD, пайплайны (модули 3–4)
- **Backend Architect** — API, архитектура (модуль 5)
- **Rapid Prototyper** — быстрые MVP (модуль 6)
- **Reality Checker** — проверка готовности к продакшну

**Установка:**
```bash
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
./scripts/convert.sh
./scripts/install.sh --tool cursor
```

Подробнее: [интеграция agency-agents](../../integrations/agency-agents.md)

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## ✅ Чек-лист

- [ ] Cursor установлен и открывает папку проекта
- [ ] Я умею дать контекст (какие файлы/папки важны) и получить правку кода
- [ ] Я понимаю, когда использовать чат, а когда inline-редактирование

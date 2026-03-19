# A6: Data Quality + reproducibility (DataOps-lite)

## 🎯 Цели урока

- Делать базовые проверки качества данных (schema/null/range/uniqueness)
- Делать анализ воспроизводимым (структура проекта, зависимости, артефакты)
- Подключить минимум CI: проверка форматирования/линта/ноутбуков (по возможности)

## ⏱️ Сколько времени

Ориентир: **2–4 часа**.

## 📺 Видео

- [Все видео курса](../../../resources/videos.md)

## 📖 Теория (минимум)

Минимальный набор data checks:
- schema (типы/колонки),
- null checks,
- range checks,
- uniqueness (id не должен дублироваться),
- “отношения” (например, FK существует).

## 🧾 Шпаргалка

См. [cheatsheet.md](cheatsheet.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md) и [prompts-library/for-security.md](../../../prompts-library/for-security.md) (про secrets).

## ✅ Чек-лист

- [ ] У меня есть 5+ data checks
- [ ] Я могу воспроизвести анализ “с нуля” по README
- [ ] Секретов/ключей нет в репозитории


# Модуль 3: Docker

Упаковка приложений в контейнеры — "у меня работает" станет "у всех работает".

## Зачем этот модуль

- Сделать запуск проекта **воспроизводимым** (одинаково у всех и в CI)
- Научиться собирать образы, запускать контейнеры и связывать несколько сервисов
- Освоить минимальную безопасность образов (не root, `.dockerignore`, scan)

## Уроки

1. [Урок 3.1: Что такое Docker](lesson-01-what-is-docker/)
2. [Урок 3.2: Dockerfile](lesson-02-dockerfile/)
3. [Урок 3.3: Docker Compose](lesson-03-docker-compose/)
4. [Урок 3.4: Безопасность](lesson-04-security/)

## Быстрые ссылки (шпаргалки)

- 3.1: [cheatsheet.md](lesson-01-what-is-docker/cheatsheet.md) — команды Docker (build/run/ps/logs)
- 3.2: [cheatsheet.md](lesson-02-dockerfile/cheatsheet.md) — Dockerfile директивы + частые проблемы
- 3.3: [cheatsheet.md](lesson-03-docker-compose/cheatsheet.md) — docker compose команды + типовые ошибки
- 3.4: [cheatsheet.md](lesson-04-security/cheatsheet.md) — security чек‑лист + Trivy

## Артефакты по модулю (что должно получиться)

- `Dockerfile` для вашего проекта
- (желательно) `docker-compose.yml` для app + db
- `.dockerignore`
- Trivy‑отчёт (скрин/лог) и короткое описание, что сделали по HIGH/CRITICAL

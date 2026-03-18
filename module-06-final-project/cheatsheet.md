# Шпаргалка: финальный проект (модуль 6)

## Минимум “junior-ready” (коротко)

- Код в GitHub (история коммитов)
- README “как запустить”
- `/health` → 200 + JSON
- Логи (старт + ошибки, без секретов)
- Dockerfile + Compose
- Не root: `USER`
- `.dockerignore`
- CI: тесты на `push` и `pull_request`
- CD: деплой на `main`
- HTTPS URL на сервис

## Что проверять перед сдачей

1) `docker build` проходит  
2) `docker compose up` поднимает сервис  
3) `/health` отвечает после деплоя  
4) CI зелёный (tests)  
5) Секретов нет в репо (проверьте `.env`, токены, ключи)  

## Главный документ

- Чек-лист: [project-template/checklist.md](project-template/checklist.md)


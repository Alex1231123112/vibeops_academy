# Шпаргалка: полный пайплайн (урок 4.4)

## Минимум “junior-ready”

- CI: тесты на `push` и `pull_request`
- CD: деплой на `main`
- Secrets: только env vars / GitHub Secrets
- `/health`: быстрый индикатор “жив ли сервис”
- Логи: видно старт и ошибки

## Структура workflow файлов

- `.github/workflows/test.yml`
- `.github/workflows/deploy.yml`

## Типовой CI шаг (Python)

- checkout
- setup-python (cache pip)
- install dependencies
- pytest

## Типовой CD шаг (общая идея)

- триггер на `push` в `main`
- deploy hook / CLI / API провайдера
- секреты — из `${{ secrets.* }}`


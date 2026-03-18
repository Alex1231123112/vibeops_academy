# Модуль 4: CI/CD

Автоматический деплой при каждом push — от кода до продакшна.

## Зачем этот модуль

- Автоматизировать проверки качества (тесты) на каждом `push` и `pull_request`
- Научиться деплоить на облачную платформу при пуше в `main`
- Понять основы доменов и HTTPS (чтобы проект был доступен “как продукт”)
- Собрать “junior-ready” пайплайн: тесты → сборка → деплой + health/logs/secrets

## Уроки

1. [Урок 4.1: Облачные основы](lesson-01-cloud-basics/)
2. [Урок 4.2: GitHub Actions](lesson-02-github-actions/)
3. [Урок 4.3: HTTPS и домены](lesson-03-https-domains/)
4. [Урок 4.4: Полный пайплайн](lesson-04-full-pipeline/)

## Артефакты по модулю (что должно получиться)

- `.github/workflows/test.yml` — тесты на `push` и `pull_request`
- `.github/workflows/deploy.yml` (или аналог) — деплой на `main`
- Секреты в GitHub Secrets / переменных окружения (не в репо)
- HTTPS URL на задеплоенный сервис + `/health`

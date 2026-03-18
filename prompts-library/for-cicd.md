# Промпты для CI/CD

Перед использованием: см. общий шаблон промпта — [template.md](template.md).

## С agency-agents

Установите [agency-agents](https://github.com/msitarzewski/agency-agents) и используйте **DevOps Automator**:

```
Используй правила @devops-automator для настройки GitHub Actions.
```

## GitHub Actions

```
Создай workflow для GitHub Actions:
- Триггеры: push и pull_request
- Python: 3.12
- Шаги: checkout@v4, setup-python@v5 (cache pip), pip install -r requirements.txt, pytest
- Имя: Test
Требование: secrets только через GitHub Secrets, ничего не хардкодить.
```

## Деплой

```
Создай workflow для деплоя на Render:
- Триггер: push в main
- Используй Render Deploy Hook или API
- Добавь шаг с уведомлением об успехе/ошибке
Секрет deploy hook URL хранится в GitHub Secrets (например DEPLOY_HOOK_URL).
```

## Полный пайплайн

```
Нужен CI/CD для Python-проекта:
1. На push — запуск тестов
2. На push в main — деплой на Railway
3. Переменные из GitHub Secrets
Опиши структуру workflow файлов и test plan (как проверить).
```

# Промпты для CI/CD

## С agency-agents

Установите [agency-agents](https://github.com/msitarzewski/agency-agents) и используйте **DevOps Automator**:

```
Используй правила @devops-automator для настройки GitHub Actions.
```

## GitHub Actions

```
Создай workflow для GitHub Actions:
- Триггер: push в main
- Шаги: checkout, setup Python 3.12, pip install, pytest
- Имя: Test
```

## Деплой

```
Создай workflow для деплоя на Render:
- Триггер: push в main
- Используй Render Deploy Hook или API
- Добавь шаг с уведомлением об успехе/ошибке
```

## Полный пайплайн

```
Нужен CI/CD для Python-проекта:
1. На push — запуск тестов
2. На push в main — деплой на Railway
3. Переменные из GitHub Secrets
Опиши структуру workflow файлов.
```

# Промпты для AI: Урок 2.6 (Тесты)

## 1) Написать unit-тесты для функции

```
Напиши pytest-тесты для этой функции.
Нужно:
- 3-5 кейсов (включая края)
- проверка исключений через pytest.raises

Код:
[вставь функцию]
```

## 2) Добавить smoke-тест для FastAPI

```
У меня есть FastAPI приложение.
Добавь тест через TestClient, который проверяет:
- GET /health возвращает 200
- json содержит поле status = "ok" или "healthy"

Покажи структуру файлов (app.py/main.py и tests/test_app.py) и команды запуска.
```

## 3) Workflow GitHub Actions под pytest

```
Сгенерируй GitHub Actions workflow для Python проекта:
- триггеры: push и pull_request
- Python 3.12
- установка зависимостей
- запуск pytest
- используй actions/checkout и actions/setup-python, включи cache pip
```


# Шпаргалка: pytest + GitHub Actions (урок 2.6)

## pytest (локально)

| Действие | Команда |
|---|---|
| Запустить все тесты | `pytest` |
| Запустить конкретный файл | `pytest tests/test_calc.py` |
| Запустить по шаблону | `pytest -k calc` |
| Показать вывод `print()` | `pytest -s` |

## Проверка исключений

```python
import pytest

with pytest.raises(ValueError):
    divide(10, 0)
```

## Минимальный workflow для GitHub Actions (pytest)

Файл: `.github/workflows/tests.yml`

```yaml
name: tests
on: [push, pull_request]
jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"
      - run: python -m pip install -U pip
      - run: pip install -r requirements.txt
      - run: pytest
```


# Шпаргалка: GitHub Actions (урок 4.2)

## Где лежат workflow

- `.github/workflows/*.yml`

## Триггеры (самые частые)

```yaml
on: [push, pull_request]
```

или

```yaml
on:
  push:
    branches: [main]
```

## Базовые шаги для Python + pytest

- `actions/checkout@v4`
- `actions/setup-python@v5` (python-version + cache pip)
- `pip install -r requirements.txt`
- `pytest`

## Secrets

- Хранить в GitHub: Settings → Secrets and variables → Actions
- Использовать в workflow:

```yaml
env:
  TOKEN: ${{ secrets.TOKEN }}
```


# Шпаргалка: Docker Security (урок 3.4)

## Минимальный security-чек-лист Dockerfile

- Не root: `USER appuser`
- Есть `.dockerignore` (не тащим `.env`, `.git`, `.venv`, `__pycache__`)
- Базовый образ slim/минимальный
- По возможности фиксируем версии зависимостей

## Trivy (сканирование образа)

Локально:

```bash
trivy image --severity HIGH,CRITICAL --ignore-unfixed my-app:latest
```

Через контейнер (Linux/macOS):

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest \
  image --severity HIGH,CRITICAL --ignore-unfixed my-app:latest
```

## Как реагировать на результаты

- Есть **fixed version** → обновить пакет/базовый образ.
- Нет фикса (`unfixed`) → минимизировать пакеты, обновить базовый образ, зафиксировать риск (в README/issue).


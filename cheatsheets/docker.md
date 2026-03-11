# Шпаргалка: Docker

## Образы и контейнеры

| Команда | Описание |
|---------|----------|
| `docker build -t name .` | Собрать образ |
| `docker run name` | Запустить контейнер |
| `docker run -p 8000:8000 name` | С пробросом порта |
| `docker ps` | Список запущенных |
| `docker stop id` | Остановить |

## Docker Compose

| Команда | Описание |
|---------|----------|
| `docker-compose up -d` | Запустить в фоне |
| `docker-compose down` | Остановить |
| `docker-compose logs` | Логи |

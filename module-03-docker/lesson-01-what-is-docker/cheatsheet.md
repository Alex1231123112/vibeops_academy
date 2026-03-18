# Шпаргалка: Docker (урок 3.1)

## Минимум терминов

- **image** — шаблон (то, что собираем)
- **container** — запущенный экземпляр image

## Минимум команд

| Что сделать | Команда |
|---|---|
| Собрать образ | `docker build -t my-app .` |
| Запустить контейнер | `docker run --rm my-app` |
| Запустить с портом | `docker run --rm -p 8000:8000 my-app` |
| Список контейнеров | `docker ps` |
| Все контейнеры | `docker ps -a` |
| Список образов | `docker images` |
| Логи контейнера | `docker logs <container>` |
| Остановить контейнер | `docker stop <container>` |


# Шпаргалка: Docker Compose (урок 3.3)

## Команды (новый compose)

| Что сделать | Команда |
|---|---|
| Поднять сервисы | `docker compose up -d` |
| Посмотреть статус | `docker compose ps` |
| Посмотреть логи | `docker compose logs -f` |
| Остановить | `docker compose down` |
| Пересобрать app | `docker compose build` |

## Команды (старый docker-compose)

Если у вас установлен “старый” плагин/команда:
- `docker-compose up -d`
- `docker-compose down`

## Частые проблемы

- Приложение внутри контейнера слушает `127.0.0.1` → снаружи не видно. Нужно `0.0.0.0`.
- Подключение к БД по `localhost` → в compose надо использовать имя сервиса, например `db`.
- Данные Postgres пропали → нужен `volume`.


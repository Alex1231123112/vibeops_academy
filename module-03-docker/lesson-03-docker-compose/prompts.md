# Промпты для AI: Урок 3.3 (Docker Compose)

## 1) Сгенерировать compose для app + postgres

```
Сделай docker-compose.yml для:
- app: собирается из Dockerfile в текущей папке, порт 8000 наружу
- db: postgres:15-alpine, volume для данных
- app подключается к db по DATABASE_URL
Покажи полный файл и объясни ключевые поля.
```

## 2) “Почему сервис не стартует?”

```
docker compose up падает.

docker-compose.yml:
[вставь]

Логи:
[вставь docker compose logs]

Найди причину и предложи исправление.
```


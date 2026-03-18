# Домашнее задание: Docker Compose

## Задание: app + PostgreSQL в docker compose

1) Создайте `docker-compose.yml` с приложением и PostgreSQL (можно взять основу из `examples/docker-compose.with-db.yml`).  
2) Запустите: `docker compose up -d` (или `docker-compose up -d`)  
3) Проверьте, что приложение работает.  

## Критерии сдачи

- [ ] Сервисы поднимаются без ошибок
- [ ] База данных запускается и имеет volume
- [ ] Приложение подключается к БД по имени сервиса (не через localhost)

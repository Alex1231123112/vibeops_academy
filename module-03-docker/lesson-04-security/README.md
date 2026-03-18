# Урок 3.4: Безопасность Docker

## 🎯 Цели урока
- Не запускать от root
- .dockerignore
- Сканирование образов

## Почему это важно

Docker делает запуск удобным, но **по умолчанию** можно легко собрать небезопасный образ:
- процесс работает от `root`;
- в образ случайно попадают `.env`, ключи, `.git`;
- зависимости уязвимы, а мы об этом не знаем.

В этом уроке — минимальный набор, который делает образ “вменяемым” для учебного продакшна.

## 1) Не запускать от root

Идея: создать пользователя и запускать приложение от него.

Пример (фрагмент Dockerfile):

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN useradd -m appuser
USER appuser
```

**Что это даёт:** если внутри приложения уязвимость — злоумышленнику сложнее “вылезти” на уровень контейнера/хоста.

## 2) .dockerignore — не тащим лишнее

В `.dockerignore` обычно добавляют:

```
.git
.env
__pycache__
*.pyc
.venv
venv
```

**Что это даёт:** меньше размер образа, быстрее сборка, меньше шанс утечки секретов.

## 3) Пин версий и минимальные базовые образы

Рекомендации:
- использовать `python:3.12-slim` вместо “толстых” образов;
- по возможности фиксировать версии зависимостей в `requirements.txt` (`==`), чтобы сборка была воспроизводимой.

## 4) Сканирование образов (Trivy)

### Вариант A: Trivy установлен локально

```bash
trivy image --severity HIGH,CRITICAL --ignore-unfixed my-app:latest
```

### Вариант B: Trivy как контейнер (без установки)

Linux/macOS:

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest \
  image --severity HIGH,CRITICAL --ignore-unfixed my-app:latest
```

Windows/PowerShell (под Docker Desktop может отличаться; если не работает — используйте локальную установку Trivy).

### Как читать результат

- **CRITICAL/HIGH**: сначала смотрим сюда.
- **fixed version**: если есть — обновляем пакет/базовый образ.
- если фикса нет (`unfixed`) — фиксируем риск: обновляем базовый образ, минимизируем пакеты, следим за обновлениями.

## ✅ Чек-лист “готово к учебному проду”

- [ ] В Dockerfile есть `USER` (не root)
- [ ] Есть `.dockerignore`
- [ ] Базовый образ slim
- [ ] Просканировали образ Trivy и разобрали HIGH/CRITICAL

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 AI-агент

Для ревью безопасности используйте [Security Engineer](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-security-engineer.md) из agency-agents.

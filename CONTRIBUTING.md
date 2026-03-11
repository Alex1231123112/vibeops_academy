# Как внести вклад в VibeOps

Спасибо за интерес к проекту! Курс разрабатывается с использованием [agency-agents](https://github.com/msitarzewski/agency-agents) — специализированных AI-агентов.

## 🤖 Разработка с agency-agents

При написании уроков, примеров кода и материалов курса мы используем агентов из agency-agents. Рекомендуем делать то же самое.

### Установка агентов

```bash
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
./scripts/convert.sh
./scripts/install.sh --tool cursor
```

### Какие агенты использовать

| Задача | Агент | Когда вызывать |
|--------|-------|----------------|
| Написание уроков, объяснения | **Content Creator** | Тексты, структура материалов |
| Примеры кода на Python | **Backend Architect**, **Rapid Prototyper** | code-examples, templates |
| Dockerfile, docker-compose | **DevOps Automator** | Модуль 3 |
| GitHub Actions, CI/CD | **DevOps Automator** | Модуль 4 |
| API, архитектура | **Backend Architect** | Модуль 5 |
| Проверка качества | **Reality Checker** | Перед коммитом |
| Безопасность кода | **Security Engineer** | Ревью примеров |

### Примеры промптов

**Новый урок:**
```
@content-creator Создай структуру урока по [тема] для курса VibeOps.
Формат: цели, теория, примеры кода, домашнее задание, чек-лист.
```

**Пример кода:**
```
@backend-architect Напиши пример на Python для урока про [тема].
Код должен быть простым, с комментариями на русском.
```

**Docker/CI/CD:**
```
@devops-automator Создай Dockerfile для Python-приложения из requirements.txt.
```

## 👥 Роли

См. [ROLES.md](ROLES.md) — роли людей (Maintainer, Contributor, Reviewer) и AI-агентов (Content Creator, DevOps Automator и др.).

## 📁 Структура репозитория

- `module-*/` — уроки по модулям
- `prompts-library/` — готовые промпты
- `integrations/` — инструкции по интеграциям (agency-agents)
- `templates/` — шаблоны проектов

## 🔀 Pull Request

1. Создайте ветку от `main`
2. Внесите изменения (желательно с помощью агентов)
3. Проверьте через **Reality Checker**: готово ли к merge
4. Откройте PR с описанием изменений

## 📬 Вопросы

- Issues на GitHub
- Telegram: @vibeops_academy_chat

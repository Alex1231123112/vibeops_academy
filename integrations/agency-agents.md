# 🎭 The Agency: Специализированные AI-агенты

[agency-agents](https://github.com/msitarzewski/agency-agents) — коллекция из 100+ AI-агентов с чёткой специализацией, личностью и рабочими процессами. Каждый агент — эксперт в своей области.

## Зачем это нужно для VibeOps?

Вместо generic-промптов ("действуй как разработчик") вы получаете **специализированных агентов** с:
- Глубокой экспертизой в домене
- Чёткими deliverable и процессами
- Готовыми примерами кода

## Агенты, релевантные для курса

| Агент | Раздел | Когда использовать |
|-------|--------|---------------------|
| 🚀 **DevOps Automator** | Engineering | CI/CD, пайплайны, деплой, мониторинг |
| 🏗️ **Backend Architect** | Engineering | API, базы данных, микросервисы |
| 🎨 **Frontend Developer** | Engineering | React/Vue, UI, производительность |
| ⚡ **Rapid Prototyper** | Engineering | Быстрые POC, MVP, итерации |
| 🔒 **Security Engineer** | Engineering | Безопасность кода, Docker, CI/CD |
| 🎯 **Reality Checker** | Testing | Проверка готовности к продакшну |

## Установка для Cursor

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents

# 2. Сгенерируйте файлы для Cursor
./scripts/convert.sh

# 3. Установите в ваш проект
./scripts/install.sh --tool cursor
```

Агенты станут `.mdc` правилами в `.cursor/rules/` вашего проекта.

## Использование в Cursor

После установки можно вызывать агентов явно:

```
Используй правила @devops-automator для настройки GitHub Actions.
```

```
Проверь этот код через @security-engineer — готов ли к продакшну?
```

## Глобальная установка

Для использования во всех проектах:

```bash
# Создайте глобальную папку правил
mkdir -p ~/.cursor/rules/agency

# Скопируйте нужные агенты
cp agency-agents/integrations/cursor/*.mdc ~/.cursor/rules/agency/
```

## Разработка курса VibeOps

Сам курс тоже пишется с помощью agency-agents. Роли агентов и матрица задач → см. [ROLES.md](../ROLES.md).

- **Content Creator** — тексты уроков, структура материалов
- **Backend Architect** / **Rapid Prototyper** — примеры кода
- **DevOps Automator** — Docker, CI/CD материалы
- **Reality Checker** — проверка перед коммитом

Подробнее: [CONTRIBUTING.md](../CONTRIBUTING.md)

## Ссылки

- [Репозиторий](https://github.com/msitarzewski/agency-agents)
- [DevOps Automator](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-devops-automator.md) — для модулей 3–4
- [Backend Architect](https://github.com/msitarzewski/agency-agents/blob/main/engineering/engineering-backend-architect.md) — для модуля 5

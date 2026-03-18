# Промпты для AI: Урок 4.2 (GitHub Actions)

База (канонично в библиотеке):

- Шаблон: [prompts-library/template.md](../../prompts-library/template.md)
- CI/CD: [prompts-library/for-cicd.md](../../prompts-library/for-cicd.md)

Ниже — 1–2 промпта, специфичные для урока.

## 1) CI workflow под pytest (подставь название файла)

```
Сгенерируй GitHub Actions workflow для Python проекта:
- триггеры: push и pull_request
- Python 3.12
- установка зависимостей из requirements.txt
- запуск pytest
- используй actions/checkout@v4 и actions/setup-python@v5
- включи cache pip
Ответ: полный YAML файл и имя файла (например `.github/workflows/test.yml`).
```

## 3) Разбор падения workflow

```
Workflow упал.
Логи:
[вставь]

1) Найди причину
2) Дай исправление
3) Скажи, как убедиться, что фикс сработает (локально/в CI)
```


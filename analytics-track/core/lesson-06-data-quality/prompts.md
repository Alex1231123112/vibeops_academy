# Промпты для AI: A6 (data quality)

База: [prompts-library/template.md](../../../prompts-library/template.md)

## 1) “Придумай data checks”

```
Вот схема/колонки датасета:
[вставь]

Предложи 10 проверок качества:
- schema/null/range/uniqueness
Для каждой: описание + пример реализации (SQL или Python).
```

## 2) “Собери минимальный CI для проверок”

```
У меня репозиторий анализа.
Хочу, чтобы в GitHub Actions на push запускались:
- линт (опционально)
- проверки качества данных (скрипт/SQL)

Сгенерируй workflow и test plan.
```


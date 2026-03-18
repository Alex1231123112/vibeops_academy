# Промпты для AI: Урок 4.4 (Полный пайплайн)

База (канонично в библиотеке):

- Шаблон: [prompts-library/template.md](../../prompts-library/template.md)
- CI/CD: [prompts-library/for-cicd.md](../../prompts-library/for-cicd.md)

Ниже — 1–2 промпта, специфичные для “production-minimum”.

## 1) “Проверка production-minimum (P0/P1/P2)”

```
Вот мой репозиторий/описание:
[вставь]

Проверь по чек-листу:
- CI
- CD
- secrets
- /health
- logs
Дай список замечаний и что поправить (с приоритетами P0/P1/P2) + test plan.
```


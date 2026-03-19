# Матрица навыков (Analytics Track)

Цель: выпускник способен **самостоятельно** выполнить анализ данных, оформить выводы и доставить результат (отчёт/дашборд/модель) в воспроизводимом виде.

Формат: **урок → навыки → проверка → артефакт**.

---

## Core

| Урок | Навыки | Проверка | Артефакт |
|---|---|---|---|
| `core/lesson-00-analytics-cycle/` | постановка вопроса, метрика/сегмент/сравнение | 3 вопроса по шаблону | `questions.md` |
| `core/lesson-01-analytics-tooling/` | git/venv/README/контекст для AI | репо “как продукт” | репо + `requirements.txt` |
| `core/lesson-02-sql/` | join/groupby/cte/window, качество | 6 запросов + проверки | `sql/` или `queries.md` |
| `core/lesson-03-python-data/` | pandas пайплайн, чистка/агрегации | 3 метрики + отчёт | `reports/` |
| `core/lesson-04-viz-storytelling/` | графики + выводы | 3 графика + 3 вывода | `reports/` |
| `core/lesson-05-metrics-experiments/` | метрики/воронки/когорты/риски | воронка/когорта + риски | `report.md` |
| `core/lesson-06-data-quality/` | data checks + воспроизводимость | 5+ checks | `checks/` |

---

## Специализации (выбрать 1)

| Ветка | Фокус | Итоговый артефакт |
|---|---|---|
| S1 Product/Growth | продуктовые метрики, эксперименты | отчёт + рекомендации |
| S2 BI | KPI, модель данных, дашборды | дашборд + KPI dictionary |
| S3 Data Analyst | SQL/pandas углубление | EDA + 10 инсайтов |
| S4 Marketing | каналы, атрибуция, ROMI | отчёт по каналам |
| S5 Finance | юнит-экономика, прогноз | модель + сценарии |
| S6 Risk/Fraud | аномалии, rules, мониторинг | детектор + метрики |
| S7 DS-lite | baseline ML + воспроизводимость | модель + отчет |
| S8 Analytics Eng | трансформации + data tests | “мини-dwh” + tests |


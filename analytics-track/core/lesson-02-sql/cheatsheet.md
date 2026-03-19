# Шпаргалка: SQL (A2)

## Минимальный набор

```sql
SELECT ...
FROM a
JOIN b ON ...
WHERE ...
GROUP BY ...
ORDER BY ...
LIMIT ...
```

## CTE

```sql
WITH base AS (
  SELECT ...
)
SELECT * FROM base;
```

## Оконка

```sql
SELECT
  user_id,
  created_at,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at) AS rn
FROM events;
```

## Типовые проверки качества

- “Сколько строк до/после JOIN?”
- “Не удвоил ли я метрику из-за N-N?”
- “Есть ли NULL там, где не должно?”


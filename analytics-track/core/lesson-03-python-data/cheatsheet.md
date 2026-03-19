# Шпаргалка: pandas (A3)

## Загрузка

```python
import pandas as pd
df = pd.read_csv("data.csv")
```

## Merge + groupby

```python
df = a.merge(b, on="user_id", how="left")
out = df.groupby("country", as_index=False).agg(cnt=("user_id", "nunique"))
```

## Даты и фильтр

```python
df["dt"] = pd.to_datetime(df["dt"])
df = df[df["dt"] >= "2026-01-01"]
```

## Пропуски

```python
df["x"] = df["x"].fillna(0)
```


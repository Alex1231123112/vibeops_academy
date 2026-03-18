# Урок 1.7: Ошибки и исключения (errors & exceptions)

В реальном коде ошибки — норма: неверный ввод, пустые файлы, сетевые сбои. Ваша задача как разработчика — **не скрывать ошибки**, а **обрабатывать ожидаемые** и делать сообщения понятными.

## 🎯 Цели урока

- Понимать traceback: где ошибка и почему
- `try / except / else / finally`
- Ловить **конкретные** исключения (`ValueError`, `KeyError`, `IndexError`, `TypeError`)
- Разница LBYL vs EAFP (когда проверять заранее, а когда ловить исключение)
- Делать “устойчивый” ввод: повторять запрос, пока не получим корректное значение

## 📖 Теория и примеры

### 1) Минимальная обработка ValueError

```python
while True:
    raw = input("Введите число: ").strip()
    try:
        value = int(raw)
        break
    except ValueError:
        print("Это не похоже на целое число. Попробуйте ещё раз.")
print("Ок:", value)
```

### 2) EAFP vs LBYL

**LBYL** (проверяем заранее):

```python
if "key" in data:
    x = data["key"]
```

**EAFP** (пытаемся и ловим ошибку):

```python
try:
    x = data["key"]
except KeyError:
    x = None
```

В Python часто удобнее EAFP: код короче и читаемее, если ошибка — редкий случай.

### 3) Не ловите “всё подряд”

Плохо:

```python
try:
    ...
except Exception:
    pass
```

Хорошо: ловите только то, что ожидаете (например `ValueError`) и делайте понятное сообщение.

## 📁 Примеры кода

- [parse_int.py](examples/parse_int.py) — устойчивый ввод числа
- [eafp_lbyl.py](examples/eafp_lbyl.py) — сравнение подходов

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).


# Базовые типы данных в Python

*По материалам [Real Python: Data Types](https://realpython.com/python-data-types/)*

## Основные встроенные типы

| Класс | Описание | Пример |
|-------|----------|--------|
| `int` | Целые числа | `42`, `-7` |
| `float` | Дробные числа | `3.14`, `-0.5` |
| `complex` | Комплексные числа | `3+4j` |
| `str` | Строки | `"привет"` |
| `bytes`, `bytearray` | Байтовые данные | `b'hello'` |
| `bool` | Логические значения | `True`, `False` |

## Целые числа (int)

```python
>>> type(42)
<class 'int'>

>>> 123 + 456
579
```

В Python 3 целые числа не ограничены по размеру (в пределах памяти).

## Дробные числа (float)

```python
>>> 3.14
3.14

>>> type(2.5)
<class 'float'>
```

## Строки (str)

```python
>>> name = "Анна"
>>> type(name)
<class 'str'>

>>> f"Привет, {name}!"
'Привет, Анна!'
```

## Логический тип (bool)

```python
>>> is_student = True
>>> type(is_student)
<class 'bool'>
```

## Проверка типа

```python
>>> x = 42
>>> type(x)
<class 'int'>

>>> isinstance(x, int)
True
```

## Преобразование типов

```python
>>> int("42")
42

>>> float("3.14")
3.14

>>> str(42)
'42'

>>> bool(1)
True
>>> bool(0)
False
```

## Важно: input() возвращает строку

```python
age = input("Сколько вам лет? ")  # "25" — строка!
next_year = int(age) + 1          # преобразуем в int
```

## Составные типы

Помимо базовых, в Python есть:

- `list` — список
- `tuple` — кортеж
- `dict` — словарь
- `set` — множество

Они рассматриваются в отдельном уроке.

---

*Оригинал: [Real Python: Data Types](https://realpython.com/python-data-types/)*

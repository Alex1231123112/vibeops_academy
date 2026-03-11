# Урок 1.1: Переменные и типы данных

## 🎯 Цели урока
- Понять, что такое переменные
- Научиться работать с типами данных
- Узнать, какие ошибки AI делает в переменных

## 📺 Видео
- [Python для начинающих](https://www.lektorium.tv/python-dlya-nachinayushchih) (Лекториум)
- [Python: с нуля до первого проекта](https://free.eduson.academy/python-razrabotchik) (Eduson)
- [Полный список видео](../../resources/videos.md)

## 📖 Теория

### Что такое переменная?
Переменная — это контейнер для данных. Представьте коробку с наклейкой:

```python
имя_коробки = "содержимое"
```

### Основные типы данных в Python

| Тип | Описание | Пример |
|-----|----------|--------|
| int | Целые числа | `age = 25` |
| float | Дробные числа | `price = 99.99` |
| str | Строки (текст) | `name = "Анна"` |
| bool | Истина/Ложь | `is_student = True` |
| list | Список | `fruits = ["apple", "banana"]` |
| dict | Словарь | `person = {"name": "Анна", "age": 25}` |

## 🤖 Типичные ошибки AI

AI часто путает типы данных. Вот пример:

**Плохой код от AI:**
```python
age = input("Сколько вам лет? ")
next_year = age + 1  # Ошибка! age — это строка
print("В следующем году вам будет " + next_year)
```

**Как должно быть:**
```python
age = int(input("Сколько вам лет? "))  # Преобразуем в число
next_year = age + 1
print(f"В следующем году вам будет {next_year}")
```

## 📁 Примеры кода

- [01-variables.py](code-examples/01-variables.py) — базовые переменные
- [02-types.py](code-examples/02-types.py) — работа с типами
- [03-bad-code.py](code-examples/03-bad-code.py) — типичные ошибки AI

## 🎯 Промпты для AI

См. [prompts.md](prompts.md)

## 🏠 Домашнее задание

См. [homework.md](homework.md)

## ✅ Чек-лист
- [ ] Посмотрел видео
- [ ] Прочитал теорию
- [ ] Попробовал примеры в коде
- [ ] Сделал домашнее задание
- [ ] Залил код на GitHub
- [ ] Написал вопрос в чат (если что-то непонятно)

## 📚 Дополнительные материалы (актуально на 2026)

**На русском (в проекте):**
- [Переменные в Python](../../resources/translations/python-variables-ru.md)
- [Типы данных в Python](../../resources/translations/python-data-types-ru.md)

**Оригиналы:**
- [W3Schools: Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Real Python: Data Types](https://realpython.com/python-data-types/)

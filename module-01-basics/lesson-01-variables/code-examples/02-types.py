"""
Урок 1.1: Работа с типами данных
Запуск: python 02-types.py
"""

# Проверка типа
age = 25
print("Тип age:", type(age))  # <class 'int'>

name = "Анна"
print("Тип name:", type(name))  # <class 'str'>

# Преобразование типов
user_input = "42"
number = int(user_input)  # строка -> число
print("Число:", number, "тип:", type(number))

price_str = "99.99"
price = float(price_str)  # строка -> дробное число
print("Цена:", price)

# input() всегда возвращает строку!
age_input = input("Сколько вам лет? ")
# age_input — это строка! Нужно преобразовать:
age = int(age_input)
next_year = age + 1
print(f"В следующем году вам будет {next_year}")

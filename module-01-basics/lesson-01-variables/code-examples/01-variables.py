"""
Урок 1.1: Базовые переменные в Python
Запуск: python 01-variables.py
"""

# Простые переменные
name = "Анна"
age = 25
height = 1.68
is_student = True

# Вывод на экран
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height, "м")
print("Студент:", is_student)

# Изменение переменной
age = 26
print("\nЧерез год возраст будет:", age)

# Конкатенация строк (осторожно с типами!)
greeting = "Привет, " + name + "!"
print(greeting)

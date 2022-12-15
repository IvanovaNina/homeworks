# Домашнее задание #6: Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.
# Пройтись по своим предыдущим ДЗ и где возможно использовать ускоренную обработку данных.
# (достаточно 3 примеров)


# Пример №1 (Задача 1 из ДЗ 3):

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Старое решение:

# my_list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(my_list)):
#     if i % 2 == 1:
#         sum += my_list[i]
# print(f'Сумма элементов списка, стоящих на нечётных позициях равна {sum}')


# Решение c enumerate:
# my_list = [2, 3, 5, 9, 3]
# sum = 0
# for i, item in enumerate(my_list):
#         if i % 2 == 1:
#             sum += item
# print(sum)


# Пример №2.  (Задача 1 из ДЗ 2):
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Старое решение:

# num = input('Введите число: ')
# sum = 0
# for i in num:
#     if i != "." and i != "-":
#         sum = sum + int(i)
# print(sum)

# Решение с помощью map:

# num = input('Введите число: ')
#
#
# def to_integer(str):
#     return int(str) if str != "." and str != "-" else 0
#
#
# print(sum(map(to_integer, list(num))))
#
# # Или с помощью map, lambda
# print(sum(map(lambda str: int(str) if str != "." and str != "-" else 0, list(num))))

# Пример №3.  (Задача 2 из ДЗ 3):

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# Старое решение:

# import math
#
# list1 = [2, 3, 4, 5, 6]
#
# list2 = []
# length = math.ceil(len(list1) / 2)
# for i in range(length):
#     list2.append(list1[i] * list1[len(list1) - 1 - i])
#
# print(f'Произведение пар чисел списка равно {list2}')


# Решение с помощью List Comprehension:

import math

list1 = [2, 3, 4, 5, 6]
list2 = []
length = math.ceil(len(list1) / 2)
list2 = [(list1[i] * list1[len(list1) - 1 - i]) for i in range(length)]
print(f'Произведение пар чисел списка равно {list2}')

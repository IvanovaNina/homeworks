# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

num = int(input('Введите число = '))

list = [''] * num
sum = 0
for i in range(len(list)):
    result = round((1 + 1 / (i + 1)) ** (i + 1), 2)
    list[i] = (f'{i + 1} : {result}')
    sum = sum + result
print(list)
print(f'Сумма элементов равна {round(sum, 2)}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число = '))
initial = num
my_list = []
while num > 0:
    my_list.insert(0, num % 2)
    num = num // 2
print(f'Число {initial} в двоичной системе равно {"".join(map(str, my_list))}')



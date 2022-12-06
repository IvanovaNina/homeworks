# Задание 1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

n = int(input('Введите степень: '))
x = ''
for k in range(n, -1, -1):
    number = random.randint(0, 100)
    if number != 0:
        if number != 1:
            x += f'{number}'

        if k == 0:
            x += ''
        elif k == 1:
            x += '*x + '
        else:
            x += f'*x**{k} + '

x += ' = 0'
print(x)
with open('file.txt', 'w') as file:
    file.write(x)
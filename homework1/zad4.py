# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

num = input('Введите цифру, обозначающую номер четверти, от ''1'' до ''4'': ')
if num == '1':
    print('Диапазон возможных координат точек в этой четверти: x > 0 (0, ꝏ]; y > 0 (0, ꝏ].')
elif num == '2':
    print('Диапазон возможных координат точек в этой четверти: x < 0 [-ꝏ, 0); y > 0 (0, ꝏ].')
elif num == '3':
    print('Диапазон возможных координат точек в этой четверти: x < 0 [-ꝏ, 0); y < 0 [-ꝏ, 0).')
elif num == '4':
    print('Диапазон возможных координат точек в этой четверти: x > 0 (0, ꝏ]; y < 0 [-ꝏ, 0).')
else:
    print('Эта цифра не может обозначать номер четверти, введите цифру от 1 о 4.')



# Задача 2. Создайте программу для игры в "крестики - нолики".
import random

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_field():
    print('----Раунд----')
    print(f'{field[0]} | {field[1]} | {field[2]}')
    print('---------')
    print(f'{field[3]} | {field[4]} | {field[5]}')
    print('---------')
    print(f'{field[6]} | {field[7]} | {field[8]}')
    print('---------')

def is_end():
    return (field[0] == field[1] == field[2] or
            field[3] == field[4] == field[5] or
            field[6] == field[7] == field[8] or
            field[0] == field[3] == field[6] or
            field[1] == field[4] == field[7] or
            field[2] == field[5] == field[8] or
            field[0] == field[4] == field[8] or
            field[2] == field[4] == field[6])

print_field()
x = random.randint(0, 1)
print('Прошла жеребьёвка.')
count = 0
while not is_end() and count < 9:
    if x == 0:
        turn = int(input('Ваш ход: '))
        while field[turn-1] == 'X' or field[turn-1] == '0':
            turn = int(input('Ваш ход: '))
        field[turn-1] = 'X'
        x = 1
    else:
        turn = random.randint(1, len(field))
        while field[turn-1] == '0' or field[turn-1] == 'X':
            turn = random.randint(1, len(field))
        field[turn - 1] = '0'
        x = 0
    print_field()
    count += 1

if not is_end():
    print('Ничья!')
elif x == 1:
    print('Вы победили!')
else:
    print('Вы проиграли!')
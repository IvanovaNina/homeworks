# Задача 1. Создайте программу для игры с конфетами - человек против бота.
# Условие задачи: на столе лежит 150 конфет. Игрок и компьютер ходят по очереди.
# Первый ход определяется жеребьёвкой. За один ход можно взять не более 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import random

total = 150


def input_player(total):
    player = int(input('Сколько конфет возьмёшь? '))
    if total > 28:
        max = 28
    else:
        max = total
    while player < 0 or player > max:
        print(f'Введите число от 1 до {max}! ')
        player = int(input('Сколько конфет возьмёшь? '))
    return player


def round(total, x):
    if x == 0:
        number = input_player(total)
        print(f'Пользователь ввёл число: {number}')
    else:
        if total > 28 * 2:
            number = random.randint(1, 28) # интеллект=)
        elif total > 28:
            number = total - 29
        else:
            number = total

        print(f'Бот ввёл число: {number}')
    print(number, total-number)
    return number


def order(x):
    if x == 0:
        return 1
    else:
        return 0

x = random.randint(0, 1)
print('Прошла жеребьёвка.')

number = round(total, x)  # первый раунд
total = total-number
x = order(x)

while total > 0:
    number = round(total, x)
    total = total - number
    x = order(x)

if x == 0:
    print('Извини. Ты проиграл!')
else:
    print('Ура! Ты выиграл!')



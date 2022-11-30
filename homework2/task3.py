# Задача 3. Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.

import random

my_list = [1, 2, 3, 4, 5]

shuffle_list = [None] * len(my_list)
counter = 0
while counter < len(my_list):
    random_pos = random.randint(0, len(my_list)-1)
    if shuffle_list[random_pos] == None:
        shuffle_list[random_pos] = my_list[counter]
        counter = counter + 1
print('Изначальный массив =', my_list)
print('Итоговый массив =', shuffle_list)

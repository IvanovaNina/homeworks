# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

min_value = 1
max_value = 0
for i in range(len(my_list)):
    current_number = my_list[i] % 1
    if current_number != 0:
        if current_number > max_value:
            max_value = current_number
        elif current_number < min_value:
            min_value = current_number

print(f'Разница между максимальным и минимальным значением дробной части '
      f'элементов равна {round(max_value - min_value, 2)}')



# Задача 2. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def fill_dictionary(dictionary, my_list):
    for i in range(len(my_list)):
        splitted = my_list[i].split('*')

        if len(splitted) > 2:
            key = splitted[-1]
        elif len(splitted) == 2:
            key = '1'
        else:
            key = '0'

        if key in dictionary:
            dictionary[key] = dictionary[key] + int(splitted[0])
        else:
            dictionary[key] = int(splitted[0])

dictionary = {}
files = ['file1.txt', 'file2.txt']
for file in files:
    data = open(file, 'r')
    for line in data:
        print(line)
        fill_dictionary(dictionary, line.split('=')[0].split(' + '))
    data.close()

print(dictionary)
x = ''
for key in dictionary:
    if key == '0':
        x += f'{dictionary[key]} '
    elif key == '1':
        x += f'{dictionary[key]}*x + '
    else:
        x += f'{dictionary[key]}*x**{key} + '
x += '= 0'
print(x)



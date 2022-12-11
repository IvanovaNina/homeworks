# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Например, aaabbbbbccccccc = 3a5b7c

def write_file(file, count, letter):
    if count == 1:
        file.write(letter)
    else:
        file.write(str(count) + letter)

def press(file, result):
    with open(file, 'r') as text:
        with open(result, 'w') as res:
            inp_str = text.readline()
            ind = 0
            count = 1
            while ind < len(inp_str) - 1:
                if inp_str[ind] == inp_str[ind + 1]:
                    count += 1
                else:
                    write_file(res, count, inp_str[ind])
                    count = 1
                ind += 1
            write_file(res, count, inp_str[ind])


press('file.txt', 'result.txt')


def depress(file, result):
    with open(file, 'r') as text:
        with open(result, 'w') as res:
            inp_str = text.readline()
            count = ''
            for letter in inp_str:
                if letter.isdigit():
                    count = letter
                else:
                    if count != '':
                        res.write(int(count) * letter)
                    else:
                        res.write(letter)
                    count = ''


depress('result.txt', 'result2.txt')

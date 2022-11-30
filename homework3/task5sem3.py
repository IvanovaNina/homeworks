# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = 8
fibbonachi = [0, 1]
nfibbonachi = [-1, 1]
for i in range(2, k + 1):
    fibbonachi.append(fibbonachi[i - 1] + fibbonachi[i - 2])
fibbonachi.insert(0, 1)
fibbonachi.insert(0, -1)
for i in range(2, k):
    fibbonachi.insert(0, fibbonachi[1] - fibbonachi[0])
print(fibbonachi)
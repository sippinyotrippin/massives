# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j.
# Формат входных данных
# Программа получает на вход размеры массива n и m, не превосходящие 100, затем элементы массива, затем числа i и j.
# Формат выходных данных
# Выведите результат

from print_matrix_func import print_matrix


i = 2  # int(input('Enter number of column 1 of 2 you want to replace'))
j = 0  # int(input('Enter number of column 2 of 2 you want to replace'))

n = 3
m = 4
massive = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]
print_matrix(massive, n, m)
print()

for k in range(n):
    massive[k][i], massive[k][j] = massive[k][j], massive[k][i]

print_matrix(massive, n, m)

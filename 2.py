# Дано нечетное число n, не превосходящее 15.
# Создайте двумерный массив из n×n элементов, заполнив его символами "."
# (каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива,
# главную диагональ и побочную диагональ.
# В результате "*" в массиве должны образовывать изображение звездочки.
# Выведите полученный массив на экран, разделяя элементы массива пробелами.

from print_matrix_func import print_matrix


n = int(input('Number you entering must not be bigger than 15 and even: '))
if n % 2 == 0 or n > 15:
    raise KeyboardInterrupt('Number you entering must be not bigger than 15 and even')

massive = [['.'] * n for i in range(n)]
for i in range(n):
    massive[i][i] = '*'
    massive[i][n-1-i] = '*'
    massive[n // 2][i] = '*'
    massive[i][n // 2] = '*'

print_matrix(massive, n, n, 2)

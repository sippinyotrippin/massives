# Дан двумерный массив размером n×m (n и m не превосходят 1000).
# Симметричный ему относительно главной диагонали массив называется транспонированным к данному.
# Он имеет размеры m×n: строки исходного массива становятся столбцами транспонированного,
# столбцы исходного массива становятся строками транспонированного.
# Для данного массива постройте транспонированный массив и выведите его на экран.

from print_matrix_func import print_matrix


n = 3
m = 4
massive = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]
transposed_massive = []
for column in range(m):
    nested_list = []
    transposed_massive.append(nested_list)
    for row in range(n):
        nested_list.append(massive[row][column])


print_matrix(massive, n, m)
print()
print_matrix(transposed_massive, m, n)

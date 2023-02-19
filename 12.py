# Даны числа n и m. Заполните массив размером n × m в шахматном порядке:
# клетки одного цвета заполнены нулями,
# а другого цвета - заполнены числами натурального ряда сверху вниз, слева направо.
# В левом верхнем углу записано число 1.
# Формат входных данных
# Вводятся два числа n и m, не превышающие 100.
# Формат выходных данных
# Выведите полученный массив, отводя на вывод каждого элемента ровно 4 символа.

from print_matrix_func import print_matrix


n = int(input('Rows: '))
m = int(input('Columns: '))
if n > 100 or m > 100:
    raise KeyboardInterrupt("'n' and 'm' must not be higher than 100")

massive = [[0] * m for i in range(n)]
number = 1
previous = 0
for row in range(n):
    for col in range(m):
        if previous == 0:
            massive[row][col] = number
            number += 1
            previous = massive[row][col]
        elif previous != 0:
            previous = 0

print_matrix(massive, n, m, width=4)

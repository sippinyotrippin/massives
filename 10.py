# По данным числам n и m заполните двумерный массив размером n×m числами от 1 до n×m “змейкой”, как показано в примере.
# Формат входных данных
# Вводятся два числа n и m, каждое из которых не превышает 20.
# Формат выходных данных
# Выведите полученный массив, отводя на вывод каждого элемента ровно 4 символа.

from print_matrix_func import print_matrix


n = int(input('Rows: '))
m = int(input('Columns: '))

if n > 20 or m > 20:
    raise KeyboardInterrupt("'n' and 'm' must not be higher than 20")

snake_massive = []

for i in range(1, n + 1):
    if i % 2 == 0:
        row = [i for i in range(m*i, m*(i-1), -1)]
        snake_massive.append(row)
    else:
        row = [i for i in range(m*(i-1)+1, (m*i)+1)]
        snake_massive.append(row)


print_matrix(snake_massive, n, m, width=4)

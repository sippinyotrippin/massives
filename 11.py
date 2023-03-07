# По данным числам n и m заполните двумерный массив размером n×m числами от 1 до n×m “диагоналями”, как показано в примере.
# Формат входных данных
# Вводятся два числа n и m, не превышающие 100.
# Формат выходных данных
# Выведите полученный массив, отводя на вывод каждого элемента ровно 4 символа.
from print_matrix_func import print_matrix


n = int(input('Rows: '))
m = int(input('Columns: '))

numbers = [i for i in range(1, (n*m)+1)]
massive = [[0] * m for _ in range(n)]

i = 0
j = 0
while numbers:
    if j != m:
        massive[i][j] = numbers.pop(0)
    else:
        i += 1
        j = m - 1
        massive[i][m-1] = numbers.pop(0)
    row = i
    col = j
    while row + 1 < n and col - 1 >= 0:
        massive[row + 1][col - 1] = numbers.pop(0)
        row += 1
        col -= 1
    j += 1


print_matrix(massive, n, m)
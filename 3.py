# Дано число n, не превышающее 100. Создайте массив размером n×n и заполните его по следующему правилу.
# На главной диагонали должны быть записаны числа 0. На двух диагоналях,
# прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

from print_matrix_func import print_matrix


n = int(input("Your number must not be bigger than 100:  "))
if n > 100:
    raise KeyboardInterrupt("'n' must not be bigger than 100")

massive = [[0] * n for _ in range(n)]

for num in range(1, n):
    print(num)
    i = 0
    while i != n - num:
        massive[i][i+num] = num
        massive[i+num][i] = num
        i += 1

print_matrix(massive, n, n, 2)

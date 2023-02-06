# Дано число n, не превосходящее 10, и массив размером n × n.
# Проверьте, является ли этот массив симметричным относительно главной диагонали.
# Выведите слово “YES”, если массив симметричный, и слово “NO” в противном случае.

from random import randint
from print_matrix_func import print_matrix


n = int(input('Enter n - massive size n × n: '))
if n > 10:
    raise KeyboardInterrupt("'n' must not be bigger than 10 ")

massive = [
    [0, 1, 2],
    [1, 0, 1],
    [2, 1, 0]
]
i = 0
result = 0

for num in range(1, n):
    i = 0
    while i != n - num:
        if massive[i][i+num] == massive[i+num][i]:
            i += 1
            result = 1
        else:
            result = 0
            break
    break

if bool(result):
    print('YES')
else:
    print('NO')

# В кинотеатре n рядов по m мест в каждом (n и m не превосходят 20).
# В двумерном массиве хранится информация о проданных билетах, число 1 означает,
# что билет на данное место уже продан, число 0 означает, что место свободно.
# Поступил запрос на продажу k билетов на соседние места в одном ряду. Определите, можно ли выполнить такой запрос.

# Формат входных данных
# Программа получает на вход числа n и m. Далее идет n строк, содержащих m чисел (0 или 1), разделенных пробелами.
# Затем дано число k.

# Формат выходных данных
# Программа должна вывести номер ряда, в котором есть k подряд идущих свободных мест.
# Если таких рядов несколько, то выведите номер наименьшего подходящего ряда.
# Если подходящего ряда нет, выведите число 0.

from generate_matrix_function import generate_matrix  # imports besides generate_matrix func and
# print_matrix func and randint because without these funcs it does not work
from print_matrix_func import print_matrix


n = int(input('Rows: '))
m = int(input('Columns: '))

if n > 20 or m > 20:
    raise KeyboardInterrupt("Maximum amount of rows and columns is 20")

k = int(input('How many tickets you want to buy? '))
massive = generate_matrix(n, m)

count = 0

for row in range(n):
    if count == k:
        print(f"{k} places in {row} row available")
        break
    else:
        count = 0

    for seat in range(m):
        if massive[row][seat] == 0 and massive[row][seat - 1] == massive[row][seat]:
            count += 1
        if count == k:
            break


print_matrix(massive, n, m)

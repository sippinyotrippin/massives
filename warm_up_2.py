# В произвольной квадратной матрице главную диагональ заполнить нулями

my_matrix = [
    [3, 78, 5],
    [26, 31, 44],
    [98, 567, 9]
]
n = 0
for _ in my_matrix:
    n += 1

for i in range(n):
    my_matrix[i][i] = 0

for row in range(n):
    for col in range(n):
        print(str(my_matrix[row][col]).rjust(5), end=' ')
    print()



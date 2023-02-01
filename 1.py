# Найдите индексы первого вхождения максимального элемента.
# Формат входных данных
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой. n и m не превышают 100.
# Формат выходных данных
# Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца

n = 3
m = 4
massive = [
    [340000, 1000, 45, 23],
    [54, 6, 32, 7],
    [5, 32, 7800, 37]
]
max_element = massive[0][0]
max_row = 0
max_column = 0
previous_max = max_element
row = 0

while row != n:
    for col in range(m):
        if massive[row][col] == max(massive[row]) and max(massive[row]) > previous_max:
            max_element = max(massive[row])
            max_row = row
            max_column = col
            previous_max = max(massive[row])
            print(massive[row][col])
            break
    row += 1

print(max_element, max_row, max_column)

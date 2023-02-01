# Дана двумерная матрица произвольного размера
# Найти сумму ее чисел
# Найти минимальный и максимальный элементы матрицы

my_matrix = [
    [164, 35, 90],
    [6532, 87, 420],
    [27, 30, 49]
]
summ = 0
min_element, max_element = my_matrix[0][0], my_matrix[0][0]
for row in my_matrix:
    if min(row) < min_element:
        min_element = min(row)
    if max(row) > max_element:
        max_element = max(row)
    for element in row:
        summ += element
print(f"Sum is {summ}")
print(f"Max element is {max_element}")
print(f"Min element is {min_element}")

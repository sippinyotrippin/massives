from random import randint


def generate_matrix(rows: int, columns: int):
    matrix = []
    for row in range(rows):
        nested_list = []
        matrix.append(nested_list)
        for col in range(columns):
            nested_list.append(randint(0, 1))

    return matrix

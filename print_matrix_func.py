def print_matrix(matrix: list, rows: int, columns: int, width: int):
    for row in range(rows):
        for col in range(columns):
            print(str(matrix[row][col]).rjust(width), end=' ')
        print()

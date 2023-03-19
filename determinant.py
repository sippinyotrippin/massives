def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        for i in range(len(matrix)):
            a = matrix[i].pop(0)
            a = a * (-1)**(i+2)
            del matrix[i]
            for j in range(len(matrix)-1):
                del matrix[j][0]
            return a * determinant(matrix)


arr = [
    [1, 2, 3, 4],
    [4, 1, 2, 3],
    [3, 4, 1, 2],
    [2, 3, 4, 1]
]
print(determinant(arr)) # should be -160

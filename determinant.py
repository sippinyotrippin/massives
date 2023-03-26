def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        result = 0
        for i in range(len(matrix)):
            minor = [0 for i in range(len(matrix)-1)]
            a = matrix[i][0] * (-1)**(i+2)
            cross = i
            j = 0
            k = 0
            while j != len(matrix) - 1:
                if k != cross:
                    minor[j] = matrix[k][1:]
                    j += 1
                    k += 1
                else:
                    k += 1
            result += a * determinant(minor)
        return result

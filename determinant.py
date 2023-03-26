from copy import deepcopy


def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        result = 0

        for i in range(len(matrix)):
            minor = deepcopy(matrix)
            a = matrix[i][0]
            a = a * (-1)**(i+2)
            del minor[i]
            for j in range(len(minor)):
                del minor[j][0]
            r = a * determinant(minor)
            result += r
        return result


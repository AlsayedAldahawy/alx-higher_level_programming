#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))


matrix = [
    [1, 2],
    [3, 4]
    ]
matrix_b = [
    [5, 6, 7],
    [8, 9, 10]
    ]
print(lazy_matrix_mul(matrix, matrix_b))

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6, 7], [8, 9, 10]]
lazy_matrix_mul(matrixA, matrixB)

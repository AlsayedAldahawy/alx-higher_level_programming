#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))


incompatible_matrix = [
    [1, 2],
    [3, 4]
    ]
incompatible_matrix_b = [
    [5, 6, 7],
    [8, 9, 10]
    ]
print(matrix_mul(incompatible_matrix, incompatible_matrix_b))

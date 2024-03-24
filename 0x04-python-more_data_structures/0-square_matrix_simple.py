#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # new_matrix = [[(x ** 2) for x in row] for row in matrix]

    new_matrix = []

    for row in matrix:
        sub = []
        for i in row:
            sub.append(i ** 2)
        new_matrix.append(sub)
    return new_matrix

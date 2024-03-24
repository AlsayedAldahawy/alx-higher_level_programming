#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # 1- using Nested List Comprehensions
    new_matrix = [[(x ** 2) for x in row] for row in matrix]

    # 2- using loops
    # new_matrix = []
    # for row in matrix:
    #     sub = []
    #     for i in row:
    #         sub.append(i ** 2)
    #     new_matrix.append(sub)

    # 3- using lambda & map
    # new_matrix = []
    # for row in matrix:
    #     new_row = list(map(lambda x: x ** 2, row))
    #     new_matrix.append(new_row)

    return new_matrix

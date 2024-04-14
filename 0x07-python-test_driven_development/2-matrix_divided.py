#!/usr/bin/python3

'''
module contains matrix_division function
'''


def matrix_divided(matrix, div):
    '''
    func that divide all elements of a matrix (list of lists)
        Args:
            matrix (list of lists): the matrix.
            div (int or float): the denominator of the division operation.
        Returns:
            int: The sum of a and b.
        Raises:
            TypeError: If matrix is not list of lists of numbers
                        or the lists have different lengths
                        or div is not an integer or float.
            ZeroDivisionError: if div == 0.
    '''

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    # checking if matrix is a list type.
    if type(matrix) is not list or matrix is None:
        raise TypeError(matrix_error)

    for i in matrix:

        # checking the matrix is list of lists
        if type(i) is not list or i is None:
            raise TypeError(matrix_error)

        # checking if all elements are numbers
        for j in i:
            if type(j) not in (int, float) or j is None:
                raise TypeError(matrix_error)

        # checking if all the lists inside the matrix are the same length
        if type(i) is list and len(i) is not len(matrix[-1]):
            raise TypeError("Each row of the matrix must have the same size")

    # checking the div type
    if type(div) not in (float, int) or div is None:
        raise TypeError('div must be a number')

    # checking the div value
    if div == 0:
        raise ZeroDivisionError("division by zero")

    results = [[round(i / div, 2) for i in y] for y in matrix]
    return results

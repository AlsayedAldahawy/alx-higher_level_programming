#!/usr/bin/python3
"""
Generates Pascal's triangle up to the specified number of rows.

Args:
    n (int): The number of rows in the Pascal's triangle.

Returns:
    list: A list of lists representing Pascal's triangle.

Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    lst = []
    prv_list = []

    if n <= 0:
        return lst

    for i in range(n):
        sublist = [None] * (i + 1)
        sublist[0], sublist[-1] = 1, 1

        j = 1
        while j < i:
            sublist[j] = prv_list[j - 1] + prv_list[j]
            j += 1

        prv_list = sublist
        lst.append(sublist)

    return lst


'''
Explaining the algorithm of Pascal tringle:

Each element in every row, except for the first and last elements,\
    is the sum of the two adjacent elements in the previous row: the one at\
        the same position and the one immediately before it.

                 1
                1+1
              1+(2)+1      2 = 1+1
            1+(3)+(3)+1    3 = 1+(2), 3 = (2)+1
          1+(4)+(6)+(4)+1  4 = 1+(3), 6 = (3)+(3), 4 = (3)+1

'''

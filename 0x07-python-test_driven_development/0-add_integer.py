#!/usr/bin/python3

"""
func that add integer
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.
    Returns:
        int: The sum of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
"""


def add_integer(a, b=98):

    """
    function to add two int
    """

    if type(a) not in [float, int] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

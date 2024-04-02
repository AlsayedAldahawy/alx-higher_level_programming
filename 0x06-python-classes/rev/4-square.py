#!/usr/bin/python3
"""Area of a square

    Raises:
        TypeError: _description_
        ValueError: _description_
    """


class Square:
    """Area of a square

    Attributes:
        __size (int): the size of square

    Raises:
        TypeError: _description_
        ValueError: _description_
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get current square area"""
        return self.__size ** 2

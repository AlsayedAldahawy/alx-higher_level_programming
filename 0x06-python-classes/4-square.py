#!/usr/bin/python3
'''square class'''


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.set_size(size)

    def area(self):
        return self.__size ** 2

    def get_size(self):
        return self.__size

    def set_size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    size = property(get_size, set_size)

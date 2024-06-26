#!/usr/bin/python3

'''square class'''


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

        # for i in range(self.__size):
        #     for j in range(self.__size):
        #         print("#", end="")
        #     print()
        # if self.__size == 0:
        #     print()

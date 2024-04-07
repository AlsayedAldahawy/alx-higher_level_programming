#!/usr/bin/python3

'''square class'''


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2) or \
              not isinstance(value[0], int) or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""

        string = ""
        if self.__size == 0:
            string += "\n"
        else:
            string += "\n" * self.__position[1]
            for i in range(self.__size):
                string += (" " * self.__position[0] + "#" * self.__size + '\n')
        return string[:-1]

        # Another method
        # if self.__size != 0:
        #     [print("") for i in range(0, self.__position[1])]
        # for i in range(0, self.__size):
        #     [print(" ", end="") for j in range(0, self.__position[0])]
        #     [print("#", end="") for k in range(0, self.__size)]
        #     if i != self.__size - 1:
        #         print("")
        # return ("")

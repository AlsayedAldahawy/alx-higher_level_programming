#!/usr/bin/python3

"""
Module: 10-square.py

This module defines the Square class, which inherits from the Rectangle class.

Classes:
    - Square: Represents a square with equal sides.

Example usage:
    >>> square = Square(5)
    >>> square.area()
    25
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class represents a square with equal sides.

    Attributes:
        - __size (int): The size of the square's sides.

    Methods:
        - __init__(self, size): Initializes a Square instance with the\
            given size.
        - area(self): Calculates and returns the area of the square.

    Example:
        >>> square = Square(5)
        >>> square.area()
        25
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.

        Example:
            >>> square = Square(5)
            >>> square.area()
            25
        """
        return self.__size ** 2

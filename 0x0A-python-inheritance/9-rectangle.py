#!/usr/bin/python3

"""
Module: 9-rectangle.py

This module defines the Rectangle class, which inherits from the\
    BaseGeometry class.

Classes:
    - Rectangle: Represents a rectangle with width and height.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle with width and height.

    Attributes:
        - __width (int): The width of the rectangle.
        - __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        Example:
            >>> rectangle = Rectangle(5, 3)
            >>> rectangle.area()
            15
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A formatted string representing the Rectangle.

        Example:
            >>> rectangle = Rectangle(5, 3)
            >>> print(rectangle)
            [Rectangle] 5/3
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

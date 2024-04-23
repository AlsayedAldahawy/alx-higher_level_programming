#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Module: 8-rectangle.py

This module defines the Rectangle class, which inherits from the\
    BaseGeometry class.

Classes:
    - Rectangle: Represents a rectangle with width and height.
"""


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

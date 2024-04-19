#!/usr/bin/python3

'''
    Module contains class Rectangle
'''


class Rectangle:
    """
    Represents a rectangle with width and height attributes.

    Attributes:
        width (int): Width of the rectangle.
            Must be an integer; otherwise, a TypeError is raised.
            If width is less than 0, a ValueError is raised.
        height (int): Height of the rectangle.
            Must be an integer; otherwise, a TypeError is raised.
            If height is less than 0, a ValueError is raised.

    Methods:
        __init__(self, width=0, height=0):
         """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.

        Args:
            width (int, optional): Width of the rectangle (default is 0).
            height (int, optional): Height of the rectangle (default is 0).
            """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return (self.__height)

    @property
    def width(self):
        return (self.__width)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

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
        Class Attributes:
        number_of_instances (int): tracks total number of Rectangle instances.
            Initialized to 0.
            Incremented during each new instance instantiation.
            Decremented during each instance deletion.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a Rectangle object with optional width and height.

        area(self):
            Calculates and returns the area of the rectangle.

        perimeter(self):
            Calculates and returns the perimeter of the rectangle.
            If width or height is equal to 0, the perimeter is 0.

        __str__(self):
            Returns a string representation of the rectangle.
            The string consists of '#' symbols forming the rectangle,
            with each row separated by newline characters.

        __repr__(self):
            Returns a string representation of the Rectangle object.
            The format of the returned string is "Rectangle(width, height)".

        __del__(self):
            Prints "Bye rectangle..." when instance of Rectangle is deleted.
         """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.

        Args:
            width (int, optional): Width of the rectangle (default is 0).
            height (int, optional): Height of the rectangle (default is 0).
            """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String containing '#' symbols forming the rectangle.
        """

        if self.height == 0 or self.width == 0:
            return ""

        # Create a string with '#' symbols for each row
        rect_str = "\n".join(["#" * self.width for _ in range(self.height)])
        return rect_str

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object.

        The format of the returned string is "Rectangle(width, height)".

        Returns:
            str: A formatted string representing the Rectangle.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Prints "Bye rectangle..." when an instance of Rectangle is deleted.
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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
        print_symbol (any): Symbol used for string representation.
            Can be of any type.

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


        Static methods:
        bigger_or_equal: to return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First rectangle instance.
            rect_2 (Rectangle): Second rectangle instance.

        Returns:
            Rectangle: The rectangle with the larger area.
                If both rectangles have the same area, returns rect_1.
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Class methods:

        square(cls, size): Creates new Rectangle instance with
            equal width and height which is square.

        Args:
            size (int, optional): Size of the square (default is 0).

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
         """
    number_of_instances = 0
    print_symbol = '#'

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
            str: containing the specified print_symbol forming the rectangle.
        """

        if self.height == 0 or self.width == 0:
            return ""

        rect_str = "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)])
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

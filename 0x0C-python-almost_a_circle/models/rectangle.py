#!/usr/bin/python3

'''
    Module "rectangle.py" contains the Rectangle class.
'''


from models.base import Base


class Rectangle(Base):
    '''
    Rectangle Class (Inherits from Base)

    This class represents a rectangle and inherits from the Base class.\
        It provides properties for width, height, x-coordinate,\
            and y-coordinate.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): x-coordinate of the top-left corner.
        __y (int): y-coordinate of the top-left corner.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new instance of the Rectangle class.
            - width: Width of the rectangle.
            - height: Height of the rectangle.
            - x: x-coordinate (optional, default is 0).
            - y: y-coordinate (optional, default is 0).
            - id: Unique ID (optional).

        Properties:
            - width: Get or set the width of the rectangle.
            - height: Get or set the height of the rectangle.
            - x: Get or set the x-coordinate of the top-left corner.
            - y: Get or set the y-coordinate of the top-left corner.

    Usage:
    1. Create an instance of the Rectangle class:
       ```
       rect1 = Rectangle(width=10, height=5)
       rect2 = Rectangle(width=8, height=3, x=2, y=4, id=100)
       ```

    2. Access properties:
       ```
       print(rect1.width)  # Prints the width (10)
       rect1.height = 7   # Sets the height to 7
       ```

    Note:
    - The Rectangle class inherits from the Base class, which provides a\
        unique ID for each instance.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        Get the width of the rectangle.

        Returns:
            int: Width value.
        '''
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Get the height of the rectangle.

        Returns:
            int: Height value.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Get the x-coordinate of the top-left corner.

        Returns:
            int: x-coordinate value.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Get the y-coordinate of the top-left corner.

        Returns:
            int: y-coordinate value.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        '''
        display rect
        '''
        for i in range(self.height):
            print("#" * self.width)

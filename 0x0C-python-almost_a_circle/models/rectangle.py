#!/usr/bin/python3

'''
    Module "rectangle.py" contains the Rectangle class.

    This module defines the Rectangle class, which inherits\
        from the Base class.
    The Rectangle class represents a geometric rectangle with\
        properties such as width, height, position (x, y), and\
            an optional unique identifier (id).
'''


from models.base import Base


class Rectangle(Base):
    '''
    Attributes:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate (horizontal position) of the top-left corner.
        - y (int): Y-coordinate (vertical position) of the top-left corner.
        - id (int): Unique identifier for the rectangle (inherited from Base).

    Methods:
        - __init__(self, width, height, x=0, y=0, id=None): Constructor\
            to initialize the rectangle.
        - display(self): Displays the rectangle using '#' characters.
        - area(self): Calculates and returns the area of the rectangle.
        - to_dictionary(self): Returns a dictionary representation of the\
            rectangle.

    Example Usage:
        rect = Rectangle(5, 3, 2, 1, 42)
        print(rect)  # Output: "[Rectangle] (42) 2/1 - 5/3"
        print(rect.area())  # Output: 15
        print(rect.to_dictionary())  # Output: {'x': 2, 'y': 1, 'id': 42,\
        'height': 3, 'width': 5}
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate (horizontal position) of the\
                top-left corner. Defaults to 0.
            y (int, optional): Y-coordinate (vertical position) of the\
                top-left corner. Defaults to 0.
            id (int, optional): Unique identifier for the rectangle.\
                Defaults to None (inherited from Base).
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the object.

        Returns:
            int: The width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the object.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the object.

        Returns:
            int: The height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the object.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the object.

        Returns:
            int: The x-coordinate value.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the object.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the object.

        Returns:
            int: The y-coordinate value.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the object.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        '''
        Displays the rectangle using '#' characters.
        '''
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''
        Returns a string representation of the rectangle.

        Returns:
            str: Formatted string containing rectangle information.
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
        Updates the rectangle attributes based on provided arguments or\
            keyword arguments.

        Args:
            *args: Variable-length argument list (id, width, height, x, y).
            **kwargs: Arbitrary keyword arguments (attribute=value pairs).
        '''
        try:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        except Exception:
            raise

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def area(self):
        '''
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        '''
        return (self.width * self.height)

    def to_dictionary(self):
        '''
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: Dictionary containing rectangle attributes.
        '''
        return {"x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width}

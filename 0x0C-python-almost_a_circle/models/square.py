#!/usr/bin/python3

'''
    square module
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle where all\
        sides are equal.

    Args:
        size (int): The size (side length) of the square.
        x (int, optional): The x-coordinate of the square's position\
            (default is 0).
        y (int, optional): The y-coordinate of the square's position\
            (default is 0).
        id (int, optional): An optional unique identifier for the square\
            (default is None).

    Attributes:
        Inherits attributes from the Rectangle class (width, height, x, y, id).

    Example usage:
        square1 = Square(size=50, x=10, y=20)
        square2 = Square(size=70, id=2)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size (side length) of the square.
            x (int, optional): The x-coordinate of the square's position\
                (default is 0).
            y (int, optional): The y-coordinate of the square's position\
                (default is 0).
            id (int, optional): An optional unique identifier for the square\
                (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
            str: A formatted string containing information about the square.
                Example: "[Square] (1) 10/20 - 50"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square.

        Args:
            value (int): The new size value.

        Notes:
            This setter updates both the width and height to maintain square\
                proportions.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the object using either keyword arguments or\
            positional arguments.

        Args:
            *args: Positional arguments (in the order: id, size, x, y).
            **kwargs: Keyword arguments (keys: "id", "size", "x", "y").

        Raises:
            IndexError: If fewer than four positional arguments are provided.

        Example usage:
            obj = Square()
            obj.update(id=1, size=50, x=10, y=20)
            # OR
            obj.update(1, 50, 10, 20)
        """
        try:
            for key, value in kwargs.items():
                if key in ["size", "x", "y", "id"]:
                    setattr(self, key, value)
        except Exception:
            raise

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Converts the attributes of the object to a dictionary.

        Returns:
            dict: A dictionary containing the following keys:
                - "id": The unique identifier of the object.
                - "x": The x-coordinate of the object.
                - "size": The size (or side length) of the object.
                - "y": The y-coordinate of the object.
        """
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}

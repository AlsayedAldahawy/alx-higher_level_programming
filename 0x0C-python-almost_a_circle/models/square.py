#!/usr/bin/python3

'''
    square module
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the print() and str() representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' update'''

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
        """return dictionary of attributes"""
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}

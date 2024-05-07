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
        return "[Square] (%d) %d/%d - %d" % (self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

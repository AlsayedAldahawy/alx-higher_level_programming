#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self, size):
        return size * size

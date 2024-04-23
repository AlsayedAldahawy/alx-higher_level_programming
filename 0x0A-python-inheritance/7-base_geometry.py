#!/usr/bin/python3

"""
Module: 6-base_geometry.py

This module defines the BaseGeometry class, which serves as a base for\
    other geometry-related classes.

Classes:
    - BaseGeometry: A base class with an abstract method area().

Example usage:
    >>> geometry = BaseGeometry()
    >>> geometry.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented.
"""


class BaseGeometry:
    """
    BaseGeometry class provides a foundation for other geometry-related\
        classes.

    Methods:
        - area(): Raises an Exception with the message "area() is not\
            implemented."

    Example:
        >>> geometry = BaseGeometry()
        >>> geometry.area()
        Traceback (most recent call last):
            ...
        Exception: area() is not implemented.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."

        Example:
            >>> geometry = BaseGeometry()
            >>> geometry.area()
            Traceback (most recent call last):
                ...
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates whether the given value is a positive integer.

        Args:
            name (str): The name of the value being validated\
                (used in error messages).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

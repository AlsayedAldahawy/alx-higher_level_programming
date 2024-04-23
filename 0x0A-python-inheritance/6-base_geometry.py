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

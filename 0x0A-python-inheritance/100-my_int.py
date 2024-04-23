#!/usr/bin/python3

"""
Module: 100-my_int.py

This module defines A custom integer class with inverted equality and\
    inequality operators.
"""


class MyInt(int):
    """
    A custom integer class with inverted equality and inequality operators.

    This class inherits from the built-in `int` class and modifies the behavior
    of the `==` and `!=` operators.

    Attributes:
        None

    Methods:
        __eq__(self, other): Inverts the behavior of the equality operator.
        __ne__(self, other): Inverts the behavior of the inequality operator.
    """

    def __eq__(self, other):
        """
        Compare two MyInt instances for equality.

        Args:
            other (MyInt or int): The other instance to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        # return False
        # return int(self) != other
        # return super().__ne__(other)
        return int.__ne__(self, other)
        # all the above solutions work the same

    def __ne__(self, other):
        """
        Compare two MyInt instances for inequality.

        Args:
            other (MyInt or int): The other instance to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        # return True
        # return int(self) == other
        return super().__eq__(other)
        # return int.__eq__(self, other)
        # all the above solutions work the same

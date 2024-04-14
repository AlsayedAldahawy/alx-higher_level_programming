#!/usr/bin/python3

"""
    module contains say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the provided first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        John Doe

        >>> say_my_name("Alice")
        Alice
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(first_name, last_name)

#!/usr/bin/python3
"""Check if object is exactly an instance of the specified class."""


def inherits_from(obj, a_class):
    """Check if object is exactly an instance of specified class

    Args:
        obj (_type_): input object
        a_class (_type_): input class

    Returns:
        _type_: True of the same, otherwise False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)

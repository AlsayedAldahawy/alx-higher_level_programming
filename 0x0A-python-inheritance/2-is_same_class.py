#!/usr/bin/python3
'''
Module contains is_same_class function
'''


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class.

    Args:
        obj: Any Python object.
        a_class: A class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

    # print(type(obj), a_class)
    # <class 'int'> <class 'int'>
    # <class 'int'> <class 'float'>
    # <class 'int'> <class 'object'>

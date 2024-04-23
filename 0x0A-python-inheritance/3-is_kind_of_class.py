#!/usr/bin/python3
'''
    Module contains is_kind_of_class function
'''


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class or any of\
        its subclasses.

    Args:
        obj: Any Python object.
        a_class: A class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,\
            False otherwise.
    """
    return (isinstance(obj, a_class))

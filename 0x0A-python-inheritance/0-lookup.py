#!/usr/bin/python3

'''
This module defines a function called `lookup`.
'''


def lookup(obj):
    """
    `lookup` takes an object as input and returns a list of its attributes\
        and methods.

    Args:
        obj: Any Python object (e.g., class instance, module, built-in type).

    Returns:
        list: A list of attribute and method names of the input object.
    """
    return dir(obj)

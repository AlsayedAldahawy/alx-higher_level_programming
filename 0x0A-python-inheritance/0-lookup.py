#!/usr/bin/python3
'''
    Module contains lookup function
'''


def lookup(obj):
    '''
    Returns a list of valid attributes and methods of the given Python object.

    Args:
        obj: Any Python object (e.g., class instance, module, built-in type).

    Returns:
        list: A list of attribute and method names of the input object.
    '''
    return dir(obj)

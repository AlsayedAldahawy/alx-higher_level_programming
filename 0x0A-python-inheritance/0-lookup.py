#!/usr/bin/python3

def lookup(obj):
    """
    This module defines a function called `lookup` that takes an object as input and returns a list of its attributes and methods.

    Args:
        obj: Any Python object (e.g., class instance, module, built-in type).

    Returns:
        list: A list of attribute and method names of the input object.

    Example:
        >>> my_list = [1, 2, 3]
        >>> lookup(my_list)
        ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    """
    return dir(obj)

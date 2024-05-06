#!/usr/bin/python3
"""
Function that returns a dictionary description with simple data structures
(lists, dictionaries, strings, integers, and booleans) for JSON serialization\
    of an object.

Args:
    obj: The object for which to generate the dictionary description.

Returns:
    dict: A dictionary containing the attributes of the input object.

Example:
    >>> class Person:
    ...     def __init__(self, name, age):
    ...         self.name = name
    ...         self.age = age
    ...
    >>> alice = Person(name="Alice", age=30)
    >>> json_data = class_to_json(alice)
    >>> print(json_data)
    {'name': 'Alice', 'age': 30}
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of the input object's attributes.

    Args:
        obj: The object for which to generate the dictionary description.

    Returns:
        dict: A dictionary containing the attributes of the input object.
    """
    return obj.__dict__     # or return vars(obj)

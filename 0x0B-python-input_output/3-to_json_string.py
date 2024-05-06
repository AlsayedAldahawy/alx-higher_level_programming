#!/usr/bin/python3

"""
    function that returns the JSON representation of an object (string):
"""


import json


def to_json_string(my_obj):
    """
    Converts a Python object (my_obj) to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: A JSON-formatted string representing the input object.

    Example:
        >>> data = {"name": "Alice", "age": 30}
        >>> json_string = to_json_string(data)
        >>> print(json_string)
        '{"name": "Alice", "age": 30}'
    """
    return json.dumps(my_obj)

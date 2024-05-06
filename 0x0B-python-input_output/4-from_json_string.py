#!/usr/bin/python3

'''
function that returns an object (Python data structure) represented\
    by a JSON string:
'''


import json


def from_json_string(my_str):
    """
    Parses a JSON-formatted string and returns the corresponding Python object.

    Args:
        my_str (str): A JSON-formatted string to be converted.

    Returns:
        Any: The Python object representing the parsed JSON data.

    Example:
        >>> json_string = '{"name": "Alice", "age": 30}'
        >>> data = from_json_string(json_string)
        >>> print(data)
        {'name': 'Alice', 'age': 30}
    """
    return json.loads(my_str)

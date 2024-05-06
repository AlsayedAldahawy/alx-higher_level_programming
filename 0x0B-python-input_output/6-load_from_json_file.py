#!/usr/bin/python3


'''
    function that creates an Object from a “JSON file”:
'''


import json


def load_from_json_file(filename):
    """
    Loads data from a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        Any: The Python object representing the parsed JSON data.

    Example:
        >>> data = load_from_json_file("data.json")
        >>> print(data)
        {'name': 'Alice', 'age': 30}
    """
    with open(filename) as file:
        return json.load(file)

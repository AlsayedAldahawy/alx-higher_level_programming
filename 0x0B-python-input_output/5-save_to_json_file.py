#!/usr/bin/python3

'''
    function that writes an Object to a text file, using a JSON representation:
'''


import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object (my_obj) to a JSON file.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to write the JSON data to.

    Example:
        >>> data = {"name": "Alice", "age": 30}
        >>> save_to_json_file(data, "output.json")
        # The data is saved to "output.json"
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attr_name (str): The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    Returns:
        None
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError(
            "Can't add new attribute")
    setattr(obj, attr_name, attr_value)

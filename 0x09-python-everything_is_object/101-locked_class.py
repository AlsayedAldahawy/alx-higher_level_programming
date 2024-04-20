#!/usr/bin/python3

"""
Module contains LockedClass class.
"""


class LockedClass:
    """
    A class that allows only the 'first_name' attribute to be set.

    Attributes:
        first_name (str): The first name of the locked object.
    """

    def __setattr__(self, name, value):
        """
        Overrides the default __setattr__ method.

        Args:
            name (str): The name of the attribute being set.
            value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute name is not 'first_name'.
        """
        if name != "first_name":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")
        else:
            super().__setattr__(name, value)

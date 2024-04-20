#!/usr/bin/python3

"""
    Module contains LockedClass class.
"""


class LockedClass:
    """
    __slots__ is a special attribute that takes a certain pool of attribute
        names that can be used.

        Any attributes will be dynamically created by the user needs to have
        a name of the specified ones in __slot__ list,
        otherwise it will raise an AttributeError.

        even built-in attributes such as "__dict__" will not be avilable unless
        it was added to the __slots__ list.
    """

    __slots__ = ["first_name"]


'''
    in case we only wanted to prevent the user from creating attributes with
    keeping the built-in attributes "__dict__", we can use __settatr__ method.
'''

# the next example passes all the checker testcases except no.7,
# which uses __dict__ attribute in the testcase

'''
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
'''

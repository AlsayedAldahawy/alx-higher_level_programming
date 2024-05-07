#!/usr/bin/python3

'''
    Module "base.py" contains class Base
'''


class Base:
    '''
    Base Class

    This class serves as a base class for other classes. It provides a simple\
        mechanism for generating unique IDs.

    Attributes:
        __nb_objects (int): A private class variable to keep track of the\
            number of instances created.

    Methods:
        __init__(self, id=None):
            Initializes a new instance of the Base class.
            If an ID is provided, it is assigned to the instance.
            Otherwise, a unique ID is generated and assigned.

    Usage:
    1. Create an instance of the Base class:
       ```
       obj1 = Base()  # Generates a unique ID
       obj2 = Base(100)  # Assigns the provided ID (100)
       ```

    2. Access the ID of an instance:
       ```
       print(obj1.id)  # Prints the unique ID
       print(obj2.id)  # Prints the provided ID (100)
       ```
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An optional ID to assign to the instance.\
                Defaults to None.

        Returns:
            None
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):

        if not list_dictionaries:
            return "[]"
        else:
            return list_dictionaries

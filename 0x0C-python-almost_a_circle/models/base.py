#!/usr/bin/python3

'''
    Module "base.py" contains class Base
'''

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        with open(cls.__name__ + ".json", "+w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_to_j = [x.to_dictionary() for x in list_objs]
                f.write(cls.to_json_string(list_to_j))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creat class"""
        if cls.__name__ == "Rectangle":
            newIns = cls(1, 2)
        elif cls.__name__ == "Square":
            newIns = cls(1)

        newIns.update(**dictionary)
        return newIns

    @classmethod
    def load_from_file(cls):
        """load json list of instances from file"""
        try:
            with open(cls.__name__ + ".json", mode="r") as jsonFile:
                jsonLDict = jsonFile.read()
                instList = [cls.create(**i) for i in
                            cls.from_json_string(jsonLDict)]
                return instList
        except Exception:
            return []

#!/usr/bin/python3
"""
    Module contains Student class
"""


class Student:
    """
    Represents a student with first name, last name, and age attributes.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(attrs=None):
            Returns a dictionary representation of the student's attributes.
            If `attrs` is provided (a list of attribute names), only those\
                attributes are included in the dictionary.

        reload_from_json(json):
            Updates the student's attributes based on the provided JSON data.

    Example:
        >>> alice = Student(first_name="Alice", last_name="Smith", age=20)
        >>> json_data = alice.to_json()
        >>> print(json_data)
        {'first_name': 'Alice', 'last_name': 'Smith', 'age': 20}

        >>> new_data = {'first_name': 'Alicia', 'age': 21}
        >>> alice.reload_from_json(new_data)
        >>> print(alice.first_name, alice.age)
        Alicia 21
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the specified attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student's attributes.

        Args:
            attrs (list, optional): A list of attribute names to include in\
                the dictionary.
            If not provided, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is not None:
            return {attr: getattr(self, attr) for attr in attrs
                    if attr in vars(self)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the student's attributes based on the provided JSON data.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Example:
            >>> new_data = {'first_name': 'Alicia', 'age': 21}
            >>> alice.reload_from_json(new_data)
            >>> print(alice.first_name, alice.age)
            Alicia 21
        """
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
            # same as:
            '''
            for attr in json:
            if attr in vars(self):
                setattr(self, attr, json[attr])
            '''

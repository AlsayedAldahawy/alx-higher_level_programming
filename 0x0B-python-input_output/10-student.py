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
        to_json(attrs=None): Returns a dictionary representation of the\
            student's attributes.
            If `attrs` is provided (a list of attribute names), only those\
                attributes are included in the dictionary.

    Example:
        >>> alice = Student(first_name="Alice", last_name="Smith", age=20)
        >>> json_data = alice.to_json()
        >>> print(json_data)
        {'first_name': 'Alice', 'last_name': 'Smith', 'age': 20}

        >>> json_data_filtered = alice.to_json(attrs=['first_name', 'age'])
        >>> print(json_data_filtered)
        {'first_name': 'Alice', 'age': 20}
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
        if type(attrs) is list:
            dict1 = {}
            for i in attrs:
                if i in self.__dict__:
                    dict1[i] = self.__dict__[i]
            return dict1
        return self.__dict__

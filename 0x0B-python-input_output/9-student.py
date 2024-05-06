#!/usr/bin/python3
"""
    Module contains Student class
"""


class Student:
    """
A simple class representing a student.

Attributes:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.

Methods:
    to_json(): Returns a dictionary representation of the student's attributes.

Example:
    >>> alice = Student(first_name="Alice", last_name="Smith", age=20)
    >>> json_data = alice.to_json()
    >>> print(json_data)
    {'first_name': 'Alice', 'last_name': 'Smith', 'age': 20}
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

    def to_json(self):
        """
        Returns a dictionary representation of the student's attributes.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__

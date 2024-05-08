#!/usr/bin/python3

'''
    Module "base.py" contains class Base
'''

import json
import csv
import turtle
import time
import random


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        with open(cls.__name__ + ".csv", mode="w+") as csvFile:
            if list_objs is None or list_objs == []:
                csvFile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

                # for obj in list_objs:
                #     if cls.__name__ == "Rectangle":
                #         csvFile.writelines("%s,%d,%d,%d,%d\n" % (
                #             obj.id, obj.width, obj.height, obj.x, obj.y))
                #     elif cls.__name__ == "Square":
                #         csvFile.writelines("%s,%d,%d,%d\n" % (
                #             obj.id, obj.size, obj.x, obj.y))
                #     else:
                #         csvFile.writelines("z")

    @classmethod
    def load_from_file_csv(cls):
        """load drom csv"""
        try:
            with open(cls.__name__ + ".csv", mode="r") as csvFile:
                lines = csvFile.readlines()

            lstOfDicts = []
            if cls.__name__ == "Rectangle":
                dictKeys = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                dictKeys = ["id", "size", "x", "y"]

            for line in lines:
                attrDict = {key: int(value)
                            for key, value in zip(dictKeys, (line.split(",")))}
                lstOfDicts.append(attrDict)

            return [cls.create(**dict2) for dict2 in lstOfDicts]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Draws lists of rectangles and squares
        '''

        # setup

        ptr = turtle.Turtle()
        ptr.pensize(5)
        turtle.colormode(255)

        # random background color each time
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        turtle.Screen().bgcolor(r, b, g)

        time.sleep(.5)

        # Draw rectangles
        for rect in list_rectangles:

            # Random colors for each rect
            r = random.randint(0, 255)
            b = random.randint(0, 255)
            g = random.randint(0, 255)
            ptr.pencolor(r, b, g)

            ptr.penup()
            ptr.goto(rect.x, rect.y)
            ptr.pendown()
            ptr.forward(rect.width)
            ptr.left(90)
            ptr.forward(rect.height)
            ptr.left(90)
            ptr.forward(rect.width)
            ptr.left(90)
            ptr.forward(rect.height)
            ptr.left(90)

        # Draw squares
        for squr in list_squares:

            # Random colors for each squr
            r = random.randint(0, 255)
            b = random.randint(0, 255)
            g = random.randint(0, 255)
            ptr.pencolor(r, b, g)

            ptr.penup()
            ptr.goto(squr.x, squr.y)
            ptr.pendown()
            ptr.forward(squr.size)
            ptr.left(90)
            ptr.forward(squr.size)
            ptr.left(90)
            ptr.forward(squr.size)
            ptr.left(90)
            ptr.forward(squr.size)
            ptr.left(90)

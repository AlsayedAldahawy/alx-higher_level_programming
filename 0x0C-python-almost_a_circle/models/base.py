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
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries representing\
                objects.

        Returns:
            str: A JSON string containing the serialized data.

        Example usage:
            rect_dict1 = {"id": 1, "width": 50, "height": 30}
            rect_dict2 = {"id": 2, "width": 40, "height": 20}
            json_str = to_json_string([rect_dict1, rect_dict2])
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Notes:
            - The JSON file is named after the class name (e.g.,\
                "Rectangle.json" or "Square.json").
            - If list_objs is empty or None, an empty JSON array is created.
            - The attribute names are determined based on the class type.

        Example usage:
            rectangles = [rect1, rect2]
            Rectangle.save_to_file(rectangles)
            # OR
            squares = [square1, square2]
            Square.save_to_file(squares)
        """
        with open(cls.__name__ + ".json", "+w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_to_j = [x.to_dictionary() for x in list_objs]
                f.write(cls.to_json_string(list_to_j))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): A valid JSON string representing a list of\
                dictionaries.

        Returns:
            list: A list of dictionaries parsed from the JSON string.

        Example usage:
            json_str = '[{"id": 1, "width": 50, "height": 30},\
                {"id": 2, "width": 40, "height": 20}]'
            obj_list = from_json_string(json_str)
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class and initializes its attributes\
            using a dictionary.

        Args:
            **dictionary: Keyword arguments representing attribute-value pairs.

        Returns:
            YourClass: An instance of the class with attributes set based on\
                the provided dictionary.

        Example usage:
            rect_dict = {"id": 1, "width": 50, "height": 30, "x": 10, "y": 20}
            rectangle_instance = Rectangle.create(**rect_dict)
            # OR
            square_dict = {"id": 2, "size": 40, "x": 5, "y": 15}
            square_instance = Square.create(**square_dict)
        """
        if cls.__name__ == "Rectangle":
            newIns = cls(1, 2)
        elif cls.__name__ == "Square":
            newIns = cls(1)

        newIns.update(**dictionary)
        return newIns

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of objects created from the JSON data.

        Notes:
            - The JSON file should contain a list of dictionaries, each\
                representing an instance.
            - The attribute names are determined based on the class type.
            - If the JSON file does not exist or an error occurs during\
                loading, an empty list is returned.

        Example usage:
            rectangles = Rectangle.load_from_file()
            # OR
            squares = Square.load_from_file()
        """
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
        """
        Saves a list of objects to a CSV file.

        Args:
            cls (type): The class type (used to determine attribute names).
            list_objs (list): A list of objects to be saved.

        Notes:
            - If list_objs is empty or None, an empty CSV file is created.
            - The CSV file is named after the class name (e.g.,"Rectangle.csv"\
                or "Square.csv").
            - The attribute names are determined based on the class type.

        Example usage:
            Rectangle.save_to_file_csv([rect1, rect2])
            # OR
            Square.save_to_file_csv([square1, square2])
        """
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
        """
        Loads objects from a CSV file and creates instances of the class.

        Returns:
            list: A list of objects created from the CSV data.

        Notes:
            - The CSV file should have attribute values separated by commas.
            - The CSV file is named after the class name (e.g.,"Rectangle.csv"\
                or "Square.csv").
            - The attribute names are determined based on the class type.
            - If the CSV file doesn't exist or an error occurs during loading,\
                an empty list is returned.

        Example usage:
            rectangles = Rectangle.load_from_file_csv()
            # OR
            squares = Square.load_from_file_csv()
        """
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
        """
        Draws lists of rectangles and squares using Python Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.

        Returns:
            None: The function displays the shapes on the screen.

        Example usage:
            rect1 = Rectangle(x=50, y=50, width=100, height=60)
            rect2 = Rectangle(x=-30, y=-20, width=80, height=40)
            square1 = Square(x=10, y=-70, size=50)
            square2 = Square(x=-60, y=30, size=70)
            draw([rect1, rect2], [square1, square2])
        """
        # Initialize the turtle
        ptr = turtle.Turtle()
        ptr.pensize(4)
        turtle.colormode(255)

        # Set a random background color
        r, g, b = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        turtle.Screen().bgcolor(r, g, b)
        time.sleep(0.5)  # Pause briefly to appreciate the background color

        # Draw rectangles
        for rect in list_rectangles:
            ptr.showturtle()

            # Random colors for each rectangle
            r, g, b = random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)
            ptr.pencolor(r, g, b)

            ptr.penup()
            ptr.goto(rect.x, rect.y)
            ptr.pendown()
            # Draw the rectangle by moving forward twice (width and height)
            for _ in range(2):
                ptr.forward(rect.width)
                ptr.left(90)
                ptr.forward(rect.height)
                ptr.left(90)
            ptr.hideturtle()

        # Draw squares
        for squr in list_squares:
            ptr.showturtle()

            # Random colors for each square
            r, g, b = random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)
            ptr.pencolor(r, g, b)

            ptr.penup()
            ptr.goto(squr.x, squr.y)
            ptr.pendown()
            #  Draw the square by moving forward four times (each side)
            for _ in range(4):
                ptr.forward(squr.size)
                ptr.left(90)
            ptr.hideturtle()

        # Keep the window open until clicked
        turtle.exitonclick()

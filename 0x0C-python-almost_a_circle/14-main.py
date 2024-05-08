#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string(None)
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

#!/usr/bin/python3
""" 12-main """
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Square(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

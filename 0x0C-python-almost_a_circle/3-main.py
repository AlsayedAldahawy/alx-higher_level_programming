#!/usr/bin/python3
""" 3-main """
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(3, 2)
    print(r1.area())

    r2 = Square(2, 10)
    print(r2.area())

    r3 = Square(8, 7, 0, 0, 12)
    print(r3.area())

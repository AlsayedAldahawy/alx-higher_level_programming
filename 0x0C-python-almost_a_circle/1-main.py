#!/usr/bin/python3
""" 1-main """
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(10, 2)
    print(r1.id)

    r2 = Square(2, 10)
    print(r2.id)

    r3 = Square(10, 2, 0, 0, 12)
    print(r3.id)

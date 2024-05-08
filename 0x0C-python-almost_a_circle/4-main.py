#!/usr/bin/python3
""" 4-main """
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(4, 6)
    r1.display()

    print("---")

    r1 = Square(2, 2)
    r1.display()

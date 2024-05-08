#!/usr/bin/python3
""" 6-main """
from models.rectangle import Square

if __name__ == "__main__":

    r1 = Square(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Square(3, 2, 1, 0)
    r2.display()

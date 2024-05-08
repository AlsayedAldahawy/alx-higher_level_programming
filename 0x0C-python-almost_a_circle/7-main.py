#!/usr/bin/python3
""" Doc """
from models.rectangle import Square

if __name__ == "__main__":

    try:

        r1 = Square(10, 10, 10, 10)
        print(r1)

        r1.update(89)
        print(r1)

        r1.update(89, 2)
        print(r1)

        r1.update(89, 2, 3)
        print(r1)

        r1.update(89, 0, 3, 4)
        print(r1)

        r1.update(89, 2, 3, 4, 5)
        print(r1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

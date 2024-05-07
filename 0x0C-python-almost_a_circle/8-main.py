#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        r1 = Rectangle(10, 10, "10", 10)
        print(r1)

        r1.update(height=1)
        print(r1)

        r1.update(width=1, x=2)
        print(r1)

        r1.update(55, y=1, width=0, x=3, id=89)
        print(r1)

        r1.update(x=1, height=2, y=3, width=4)
        print(r1)

    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

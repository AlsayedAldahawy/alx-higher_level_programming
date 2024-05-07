#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_ids(self):
        x1 = Rectangle(1, 2)
        x2 = Rectangle(1, 2, 3, 4, None)
        x3 = Rectangle(1, 2, 3, 4, 5)
        x4 = Rectangle(1, 2, 3, 4, "5")
        self.assertEqual(x1.id, x2.id - 1)
        self.assertEqual(x2.id, x1.id + 1)
        self.assertEqual(x3.id, 5)
        self.assertEqual(x4.id, "5")

    def test_initial_args(self):
        x1 = Rectangle(1, 2)
        x2 = Rectangle(7, 8)
        x3 = Rectangle(3, 5, 3, 4, 5)

        self.assertEqual(x1.width, 1)
        self.assertEqual(x2.width, 7)
        self.assertEqual(x3.width, 3)
        self.assertEqual(x1.height, 2)
        self.assertEqual(x2.height, 8)
        self.assertEqual(x3.height, 5)
        self.assertEqual(x1.x, x2.x, 0)
        self.assertEqual(x1.y, x2.y, 0)
        self.assertEqual(x3.x, 3)
        self.assertEqual(x3.y, 4)

    def test_width_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle("1", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(None, 8)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(0, 5, 3, 4, 5)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(-1, 5, 3, 4, 5)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2, None)
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 0, 3, 4, 5)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, -1, 3, 4, 5)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, 2, "1", 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, None, 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, -1, 4, 5)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, -3, 4, 5)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, 2, 1, "2")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, 1, None)
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, 1, -4, 5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, 3, -8, 5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_area(self):
        x1 = Rectangle(5, 7, 1, 1, 20)
        x2 = Rectangle(7, 5)
        x3 = Rectangle(3, 1, 1)
        self.assertEqual(x1.area(), x2.area(), 35)
        self.assertEqual(x3.area(), 3)

    def test_str(self):
        x1 = Rectangle(2, 3, 5, 6, 10)

        self.assertEqual(str(x1), "[Rectangle] (10) 5/6 - 2/3")

        out = StringIO()
        sys.stdout = out

        print(x1)

        self.assertEqual(out.getvalue(),
                            "[Rectangle] (10) 5/6 - 2/3\n")

    def test_display(self):
        x1 = Rectangle(2, 3)

        out = StringIO()
        sys.stdout = out
        x1.display()
        x = "##\n##\n##\n"
        self.assertEqual(out.getvalue(), x)

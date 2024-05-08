#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangleInitialization(unittest.TestCase):

    def test_ids(self):
        x1 = Rectangle(1, 2)
        x2 = Rectangle(1, 2, 3, 4, None)
        x3 = Rectangle(1, 2, 3, 4, 5)
        x4 = Rectangle(1, 2, 3, 4, "5")
        x5 = Rectangle(1, 2, 3, 4, 0)
        x6 = Rectangle(1, 2, 3, 4, -7)
        self.assertEqual(x1.id, x2.id - 1)
        self.assertEqual(x2.id, x1.id + 1)
        self.assertEqual(x3.id, 5)
        self.assertEqual(x4.id, "5")
        self.assertEqual(x5.id, 0)
        self.assertEqual(x6.id, -7)

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


class TestRectInitErrors(unittest.TestCase):

    def test_miss_args(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle()
        self.assertEqual(str(
            cm.exception), "__init__() missing 2 required positional arguments: 'width' and 'height'")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2)
        self.assertEqual(
            str(cm.exception), "__init__() missing 1 required positional argument: 'height'")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x1)
        self.assertEqual(str(cm.exception),
                         "local variable 'x1' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x2)
        self.assertEqual(str(cm.exception),
                         "local variable 'x2' referenced before assignment")

    def test_width_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle("1", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(None, 8)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle((1, 2), 8)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle([(1, 2), 5], 8)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle({"key": 12}, 8)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(0, 5, 3, 4, 5)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(-1, 5, 3, 4, 5)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x1)
        self.assertEqual(str(cm.exception),
                         "local variable 'x1' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x2)
        self.assertEqual(str(cm.exception),
                         "local variable 'x2' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x3)
        self.assertEqual(str(cm.exception),
                         "local variable 'x3' referenced before assignment")

    def test_height_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2, None)
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2, (1, 2))
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2, [1, 2])
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(2, {"key": 12})
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 0, 3, 4, 5)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, -1, 3, 4, 5)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x1)
        self.assertEqual(str(cm.exception),
                         "local variable 'x1' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x2)
        self.assertEqual(str(cm.exception),
                         "local variable 'x2' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x3)
        self.assertEqual(str(cm.exception),
                         "local variable 'x3' referenced before assignment")

    def test_x_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, 2, "1", 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, None, 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, (1, 2), 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, [(1, 2), 3], 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, {"key": 12}, 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, -1, 4, 5)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, -3, 4, 5)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x1)
        self.assertEqual(str(cm.exception),
                         "local variable 'x1' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x2)
        self.assertEqual(str(cm.exception),
                         "local variable 'x2' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x3)
        self.assertEqual(str(cm.exception),
                         "local variable 'x3' referenced before assignment")

    def test_y_error(self):
        with self.assertRaises(TypeError) as cm:
            x1 = Rectangle(1, 2, 1, "2")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, 1, None)
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, 3, (1, 2))
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, 3, [(1, 2), 3])
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(TypeError) as cm:
            x2 = Rectangle(1, 2, 6, {"key": 12})
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, 1, -4, 5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as cm:
            x3 = Rectangle(5, 1, 3, -8, 5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x1)
        self.assertEqual(str(cm.exception),
                         "local variable 'x1' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x2)
        self.assertEqual(str(cm.exception),
                         "local variable 'x2' referenced before assignment")

        with self.assertRaises(UnboundLocalError) as cm:
            print(x3)
        self.assertEqual(str(cm.exception),
                         "local variable 'x3' referenced before assignment")


class TestSettersGetters(unittest.TestCase):
    def test_widthHight_SetGet(self):

        x1 = Rectangle(1, 1)
        x2 = Rectangle(1, 1)
        self.assertEqual(x1.width, x1.height, 1)
        self.assertEqual(x2.width, x2.height, 1)

        x1.width = 2
        x1.height = 3
        x2.width = 4
        x2.height = 5

        self.assertEqual(x1.width, 2)
        self.assertEqual(x1.height, 3)
        self.assertEqual(x2.width, 4)
        self.assertEqual(x2.height, 5)

    def test_xy_setGet(self):
        x1 = Rectangle(1, 1)
        x2 = Rectangle(1, 1, 2, 2)
        self.assertEqual(x1.x, x1.y, 0)
        self.assertEqual(x2.x, x2.y, 2)

        x1.x = 1
        x1.y = 3
        x2.x = 4
        x2.y = 5

        self.assertEqual(x1.x, 1)
        self.assertEqual(x1.y, 3)
        self.assertEqual(x2.x, 4)
        self.assertEqual(x2.y, 5)


class TestSetGetErrors(unittest.TestCase):

    def test_widthHight_SetGet_Er(self):

        x1 = Rectangle(1, 1)
        x2 = Rectangle(1, 1)
        x3 = Rectangle(1, 1)
        x4 = Rectangle(1, 1)
        x5 = Rectangle(1, 1)
        x6 = Rectangle(1, 1)
        x7 = Rectangle(1, 1)
        x8 = Rectangle(1, 1)
        self.assertEqual(x1.width, x1.height, 1)
        self.assertEqual(x2.width, x2.height, 1)
        self.assertEqual(x4.width, x4.height, 1)
        self.assertEqual(x6.width, x6.height, 1)
        self.assertEqual(x3.width, x3.height, 1)
        self.assertEqual(x5.width, x5.height, 1)
        self.assertEqual(x7.width, x7.height, 1)
        self.assertEqual(x8.width, x8.height, 1)

        with self.assertRaises(TypeError) as cm:
            x1.width = "1"
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(x1.width, "1")

        with self.assertRaises(TypeError) as cm:
            x2.width = None
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(x2.width, None)

        with self.assertRaises(TypeError) as cm:
            x2.width = (1, 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(x2.width, (1, 2))

        with self.assertRaises(TypeError) as cm:
            x2.width = [1, (1, 2)]
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(x2.width, [1, (1, 2)])

        with self.assertRaises(TypeError) as cm:
            x2.width = {"key": 12}
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(x2.width, {"key": 12})

        with self.assertRaises(TypeError) as cm:
            x3.height = "2"
        self.assertEqual(str(cm.exception), "height must be an integer")

        self.assertNotEqual(x3.height, "2")

        with self.assertRaises(TypeError) as cm:
            x4.height = None
        self.assertEqual(str(cm.exception), "height must be an integer")

        self.assertNotEqual(x4.height, None)

        with self.assertRaises(TypeError) as cm:
            x2.height = (1, 2)
        self.assertEqual(str(cm.exception), "height must be an integer")

        self.assertNotEqual(x2.height, (1, 2))

        with self.assertRaises(TypeError) as cm:
            x2.height = [1, (1, 2)]
        self.assertEqual(str(cm.exception), "height must be an integer")

        self.assertNotEqual(x2.height, [1, (1, 2)])

        with self.assertRaises(TypeError) as cm:
            x2.height = {"key": 12}
        self.assertEqual(str(cm.exception), "height must be an integer")

        self.assertNotEqual(x2.height, {"key": 12})

        with self.assertRaises(ValueError) as cm:
            x5.width = 0
        self.assertEqual(str(cm.exception), "width must be > 0")

        self.assertNotEqual(x5.width, 0)

        with self.assertRaises(ValueError) as cm:
            x6.width = -1
        self.assertEqual(str(cm.exception), "width must be > 0")

        self.assertNotEqual(x6.width, -1)

        with self.assertRaises(ValueError) as cm:
            x7.height = 0
        self.assertEqual(str(cm.exception), "height must be > 0")

        self.assertNotEqual(x7.height, 0)

        with self.assertRaises(ValueError) as cm:
            x8.height = -1
        self.assertEqual(str(cm.exception), "height must be > 0")

        self.assertNotEqual(x8.height, -1)

    def test_XY_SetGet_Er(self):

        x1 = Rectangle(1, 1)
        x2 = Rectangle(1, 1)
        x3 = Rectangle(1, 1)
        x4 = Rectangle(1, 1)
        x5 = Rectangle(1, 1)
        x6 = Rectangle(1, 1)
        x7 = Rectangle(1, 1)
        x8 = Rectangle(1, 1)
        self.assertEqual(x1.x, x1.y, 0)
        self.assertEqual(x2.x, x2.y, 0)
        self.assertEqual(x4.x, x4.y, 0)
        self.assertEqual(x6.x, x6.y, 0)
        self.assertEqual(x5.x, x5.y, 0)
        self.assertEqual(x3.x, x3.y, 0)
        self.assertEqual(x7.x, x7.y, 0)
        self.assertEqual(x8.x, x8.y, 0)

        with self.assertRaises(TypeError) as cm:
            x1.x = "1"
        self.assertEqual(str(cm.exception), "x must be an integer")

        self.assertNotEqual(x1.x, "1")

        with self.assertRaises(TypeError) as cm:
            x1.x = None
        self.assertEqual(str(cm.exception), "x must be an integer")

        self.assertNotEqual(x1.x, None)

        with self.assertRaises(TypeError) as cm:
            x2.x = (1, 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

        self.assertNotEqual(x2.x, (1, 2))

        with self.assertRaises(TypeError) as cm:
            x2.x = [1, 2]
        self.assertEqual(str(cm.exception), "x must be an integer")

        self.assertNotEqual(x2.x, [1, 2])

        with self.assertRaises(TypeError) as cm:
            x2.x = {"key": 12}
        self.assertEqual(str(cm.exception), "x must be an integer")

        self.assertNotEqual(x2.x, {"key": 12})

        with self.assertRaises(TypeError) as cm:
            x3.y = "2"
        self.assertEqual(str(cm.exception), "y must be an integer")

        self.assertNotEqual(x3.y, "2")

        with self.assertRaises(TypeError) as cm:
            x3.y = None
        self.assertEqual(str(cm.exception), "y must be an integer")

        self.assertNotEqual(x3.y, None)

        with self.assertRaises(TypeError) as cm:
            x3.y = (1, 2)
        self.assertEqual(str(cm.exception), "y must be an integer")

        self.assertNotEqual(x3.y, (1, 2))

        with self.assertRaises(TypeError) as cm:
            x3.y = [(1, 2), 3]
        self.assertEqual(str(cm.exception), "y must be an integer")

        self.assertNotEqual(x3.y, [(1, 2), 3])

        with self.assertRaises(TypeError) as cm:
            x3.y = {"key": 123}
        self.assertEqual(str(cm.exception), "y must be an integer")

        self.assertNotEqual(x3.y, {"key": 123})

        with self.assertRaises(ValueError) as cm:
            x5.x = -8
        self.assertEqual(str(cm.exception), "x must be >= 0")

        self.assertNotEqual(x5.x, -8)

        with self.assertRaises(ValueError) as cm:
            x6.x = -1
        self.assertEqual(str(cm.exception), "x must be >= 0")

        self.assertNotEqual(x6.x, -1)

        with self.assertRaises(ValueError) as cm:
            x7.y = -9
        self.assertEqual(str(cm.exception), "y must be >= 0")

        self.assertNotEqual(x7.y, -9)

        with self.assertRaises(ValueError) as cm:
            x8.y = -1
        self.assertEqual(str(cm.exception), "y must be >= 0")

        self.assertNotEqual(x8.y, -1)


class TestUpdate(unittest.TestCase):

    def setUp(self):
        # initiating objects with dummy attributes
        self.x1 = Rectangle(1, 1, 1, 1, 1)
        self.x2 = Rectangle(1, 1, 1, 1, 2)
        self.x3 = Rectangle(1, 1, 1, 1, 3)
        self.x4 = Rectangle(1, 1, 1, 1, 4)
        self.x5 = Rectangle(1, 1, 1, 1, 5)
        self.x6 = Rectangle(1, 1, 1, 1, 6)
        self.x7 = Rectangle(1, 1, 1, 1, 7)
        self.x8 = Rectangle(1, 1, 1, 1, 8)

    def test_0arg(self):
        self.x1.update()
        self.assertEqual(self.x1.id, self.x1.width, 1)
        self.assertEqual(self.x1.height, self.x1.x, 1)
        self.assertEqual(self.x1.y, 1)

    def test_1arg(self):
        self.x1.update()
        self.assertEqual(self.x1.id, 1)

        self.x1.update(5)
        self.assertEqual(self.x1.id, 5)

        self.x1.update(0)
        self.assertEqual(self.x1.id, 0)

        self.x1.update(-5)
        self.assertEqual(self.x1.id, -5)

        self.x1.update("5")
        self.assertEqual(self.x1.id, "5")

        self.x1.update(None)
        self.assertEqual(self.x1.id, None)

        self.x1.update((None, 'l', 7))
        self.assertEqual(self.x1.id, (None, 'l', 7))

        self.x1.update([(None, 'l', 7)])
        self.assertEqual(self.x1.id, [(None, 'l', 7)])

        self.x1.update({"key": "value"})
        self.assertEqual(self.x1.id, {"key": "value"})

        # Making sure no other attributes was affected
        self.assertEqual(self.x1.y, self.x1.width, 1)
        self.assertEqual(self.x1.height, self.x1.x, 1)

    def test_2args(self):
        self.x2.update(2, 5)
        self.assertEqual(self.x2.id, 2)
        self.assertEqual(self.x2.width, 5)

        self.x2.update("2", 5)
        self.assertEqual(self.x2.id, "2")
        self.assertEqual(self.x2.width, 5)

        self.x2.update(-2, 5)
        self.assertEqual(self.x2.id, -2)
        self.assertEqual(self.x2.width, 5)

        self.x2.update(None, 5)
        self.assertEqual(self.x2.id, None)
        self.assertEqual(self.x2.width, 5)

        self.x2.update((None, "l", 7), 5)
        self.assertEqual(self.x2.id, (None, 'l', 7))
        self.assertEqual(self.x2.width, 5)

        self.x2.update([(None, 'l', 7)], 5)
        self.assertEqual(self.x2.id, [(None, 'l', 7)])
        self.assertEqual(self.x2.width, 5)

        self.x2.update({"key": "value"}, 6)
        self.assertEqual(self.x2.id, {"key": "value"})
        self.assertEqual(self.x2.width, 6)

    def test_2args_err(self):

        with self.assertRaises(TypeError) as cm:
            self.x3.update(2, "5")
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(self.x3.width, "5")

        with self.assertRaises(TypeError) as cm:
            self.x3.update(2, None)
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(self.x3.width, None)

        with self.assertRaises(TypeError) as cm:
            self.x3.update(2, (1, 2))
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(self.x3.width, (1, 2))

        with self.assertRaises(TypeError) as cm:
            self.x3.update(2, [(1, 3), 5])
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(self.x3.width, [(1, 3), 5])

        with self.assertRaises(TypeError) as cm:
            self.x3.update(2, {"key": "5"})
        self.assertEqual(str(cm.exception), "width must be an integer")

        self.assertNotEqual(self.x3.width, {"key": "5"})

        with self.assertRaises(ValueError) as cm:
            self.x3.update(2, -5)
        self.assertEqual(str(cm.exception), "width must be > 0")

        self.assertNotEqual(self.x3.width, -5)

        with self.assertRaises(ValueError) as cm:
            self.x3.update(2, 0)
        self.assertEqual(str(cm.exception), "width must be > 0")

        self.assertNotEqual(self.x3.width, 0)

    def test_3args(self):
        self.x3.update(2, 5, 6)
        self.assertEqual(self.x3.id, 2)
        self.assertEqual(self.x3.width, 5)
        self.assertEqual(self.x3.height, 6)

        self.x3.update("2", 6, 5)
        self.assertEqual(self.x3.id, "2")
        self.assertEqual(self.x3.width, 6)
        self.assertEqual(self.x3.height, 5)

        self.x3.update(-2, 5, 6)
        self.assertEqual(self.x3.id, -2)
        self.assertEqual(self.x3.width, 5)
        self.assertEqual(self.x3.height, 6)

        self.x3.update(None, 6, 5)
        self.assertEqual(self.x3.id, None)
        self.assertEqual(self.x3.width, 6)
        self.assertEqual(self.x3.height, 5)

        self.x3.update((None, "l", 7), 5, 6)
        self.assertEqual(self.x3.id, (None, 'l', 7))
        self.assertEqual(self.x3.width, 5)
        self.assertEqual(self.x3.height, 6)

        self.x3.update([(None, 'l', 7)], 6, 5)
        self.assertEqual(self.x3.id, [(None, 'l', 7)])
        self.assertEqual(self.x3.width, 6)
        self.assertEqual(self.x3.height, 5)

        self.x3.update({"key": "value"}, 5, 6)
        self.assertEqual(self.x3.id, {"key": "value"})
        self.assertEqual(self.x3.width, 5)
        self.assertEqual(self.x3.height, 6)

    def test_3args_err(self):

        # width errors

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, "3", 4)
        self.assertEqual(str(cm.exception), "width must be an integer")
        self.assertNotEqual(self.x4.width, "3")

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, (1, 2), 4)
        self.assertEqual(str(cm.exception), "width must be an integer")
        self.assertNotEqual(self.x4.width, (1, 2))

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, [1, 2], 4)
        self.assertEqual(str(cm.exception), "width must be an integer")
        self.assertNotEqual(self.x4.width, [1, 2])

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, {"key": [1, 2]}, 4)
        self.assertEqual(str(cm.exception), "width must be an integer")
        self.assertNotEqual(self.x4.width, {"key": [1, 2]})

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, {5}, 4)
        self.assertEqual(str(cm.exception), "width must be an integer")
        self.assertNotEqual(self.x4.width, 5)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, 0, 4)
        self.assertEqual(str(cm.exception), "width must be > 0")
        self.assertNotEqual(self.x4.width, 0)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, -5, 4)
        self.assertEqual(str(cm.exception), "width must be > 0")
        self.assertNotEqual(self.x4.width, -5)

        # height errors

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, "3")
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertNotEqual(self.x4.height, "3")

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, (1, 2))
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertNotEqual(self.x4.height, (1, 2))

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, [1, 2])
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertNotEqual(self.x4.height, [1, 2])

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, {"key": [1, 2]})
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertNotEqual(self.x4.height, {"key": [1, 2]})

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, {5})
        self.assertEqual(str(cm.exception), "height must be an integer")
        self.assertNotEqual(self.x4.height, 5)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, 4, 0)
        self.assertEqual(str(cm.exception), "height must be > 0")
        self.assertNotEqual(self.x4.height, 0)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, 5, -4)
        self.assertEqual(str(cm.exception), "height must be > 0")
        self.assertNotEqual(self.x4.height, -4)

    def test_4args(self):
        self.x4.update(2, 5, 6, 8)
        self.assertEqual(self.x4.id, 2)
        self.assertEqual(self.x4.width, 5)
        self.assertEqual(self.x4.height, 6)
        self.assertEqual(self.x4.x, 8)

        self.x4.update("2", 6, 5, 7)
        self.assertEqual(self.x4.id, "2")
        self.assertEqual(self.x4.width, 6)
        self.assertEqual(self.x4.height, 5)
        self.assertEqual(self.x4.x, 7)

        self.x4.update(-2, 5, 6, 8)
        self.assertEqual(self.x4.id, -2)
        self.assertEqual(self.x4.width, 5)
        self.assertEqual(self.x4.height, 6)
        self.assertEqual(self.x4.x, 8)

        self.x4.update(None, 6, 5, 7)
        self.assertEqual(self.x4.id, None)
        self.assertEqual(self.x4.width, 6)
        self.assertEqual(self.x4.height, 5)
        self.assertEqual(self.x4.x, 7)

        self.x4.update((None, "l", 7), 5, 6, 8)
        self.assertEqual(self.x4.id, (None, 'l', 7))
        self.assertEqual(self.x4.width, 5)
        self.assertEqual(self.x4.height, 6)
        self.assertEqual(self.x4.x, 8)

        self.x4.update([(None, 'l', 7)], 6, 5, 7)
        self.assertEqual(self.x4.id, [(None, 'l', 7)])
        self.assertEqual(self.x4.width, 6)
        self.assertEqual(self.x4.height, 5)
        self.assertEqual(self.x4.x, 7)

        self.x4.update({"key": "value"}, 5, 6, 0)
        self.assertEqual(self.x4.id, {"key": "value"})
        self.assertEqual(self.x4.width, 5)
        self.assertEqual(self.x4.height, 6)
        self.assertEqual(self.x4.x, 0)

    def test_4args_err(self):
        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")
        self.assertNotEqual(self.x4.x, "3")

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 2, (1, 2))
        self.assertEqual(str(cm.exception), "x must be an integer")
        self.assertNotEqual(self.x4.x, (1, 2))

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, [1, 2])
        self.assertEqual(str(cm.exception), "x must be an integer")
        self.assertNotEqual(self.x4.x, [1, 2])

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, {"key": [1, 2]})
        self.assertEqual(str(cm.exception), "x must be an integer")
        self.assertNotEqual(self.x4.x, {"key": [1, 2]})

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, {5})
        self.assertEqual(str(cm.exception), "x must be an integer")
        self.assertNotEqual(self.x4.x, 5)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, 4, 3, -5)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        self.assertNotEqual(self.x4.x, -5)

    def test_5args(self):
        self.x5.update(2, 5, 6, 8, 7)
        self.assertEqual(self.x5.id, 2)
        self.assertEqual(self.x5.width, 5)
        self.assertEqual(self.x5.height, 6)
        self.assertEqual(self.x5.x, 8)
        self.assertEqual(self.x5.y, 7)

        self.x5.update("2", 6, 5, 7, 8)
        self.assertEqual(self.x5.id, "2")
        self.assertEqual(self.x5.width, 6)
        self.assertEqual(self.x5.height, 5)
        self.assertEqual(self.x5.x, 7)
        self.assertEqual(self.x5.y, 8)

        self.x5.update(-2, 5, 6, 8, 7)
        self.assertEqual(self.x5.id, -2)
        self.assertEqual(self.x5.width, 5)
        self.assertEqual(self.x5.height, 6)
        self.assertEqual(self.x5.x, 8)
        self.assertEqual(self.x5.y, 7)

        self.x5.update(None, 6, 5, 7, 8)
        self.assertEqual(self.x5.id, None)
        self.assertEqual(self.x5.width, 6)
        self.assertEqual(self.x5.height, 5)
        self.assertEqual(self.x5.x, 7)
        self.assertEqual(self.x5.y, 8)

        self.x5.update((None, "l", 7), 5, 6, 8, 7)
        self.assertEqual(self.x5.id, (None, 'l', 7))
        self.assertEqual(self.x5.width, 5)
        self.assertEqual(self.x5.height, 6)
        self.assertEqual(self.x5.x, 8)
        self.assertEqual(self.x5.y, 7)

        self.x5.update([(None, 'l', 7)], 6, 5, 7, 8)
        self.assertEqual(self.x5.id, [(None, 'l', 7)])
        self.assertEqual(self.x5.width, 6)
        self.assertEqual(self.x5.height, 5)
        self.assertEqual(self.x5.x, 7)
        self.assertEqual(self.x5.y, 8)

        self.x5.update({"key": "value"}, 5, 6, 0, 7)
        self.assertEqual(self.x5.id, {"key": "value"})
        self.assertEqual(self.x5.width, 5)
        self.assertEqual(self.x5.height, 6)
        self.assertEqual(self.x5.x, 0)
        self.assertEqual(self.x5.y, 7)

    def test_5args_err(self):
        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 2, 7, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")
        self.assertNotEqual(self.x4.y, "3")

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 2, 6, (1, 2))
        self.assertEqual(str(cm.exception), "y must be an integer")
        self.assertNotEqual(self.x4.y, (1, 2))

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, 4, [1, 2])
        self.assertEqual(str(cm.exception), "y must be an integer")
        self.assertNotEqual(self.x4.y, [1, 2])

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, 4, {"key": [1, 2]})
        self.assertEqual(str(cm.exception), "y must be an integer")
        self.assertNotEqual(self.x4.y, {"key": [1, 2]})

        with self.assertRaises(TypeError) as cm:
            self.x4.update(2, 4, 3, 7, {5})
        self.assertEqual(str(cm.exception), "y must be an integer")
        self.assertNotEqual(self.x4.y, 5)

        with self.assertRaises(ValueError) as cm:
            self.x4.update(2, 4, 3, 4, -5)
        self.assertEqual(str(cm.exception), "y must be >= 0")
        self.assertNotEqual(self.x4.x, -5)

    def test_more_args(self):

        # ignores the extra args
        self.x7.update(2, 5, 6, 8, 7, 9, 10, 11)
        self.assertEqual(self.x7.id, 2)
        self.assertEqual(self.x7.width, 5)
        self.assertEqual(self.x7.height, 6)
        self.assertEqual(self.x7.x, 8)
        self.assertEqual(self.x7.y, 7)


class TestArea(unittest.TestCase):
    def test_area_after_initialization(self):
        x1 = Rectangle(5, 7, 1, 1, 20)
        x2 = Rectangle(7, 5)
        x3 = Rectangle(3, 1, 1)
        self.assertEqual(x1.area(), x2.area(), 35)
        self.assertEqual(x3.area(), 3)

    def test_area_after_update(self):
        x1 = Rectangle(5, 7, 1, 1, 20)
        x2 = Rectangle(7, 5)
        x3 = Rectangle(3, 1, 1)

        x1.update(17, 2, 6, 2, 6)
        x2.update(18, 4, 3, 0, 5)
        x3.update(16, 4, 6, 5, 0)

        self.assertEqual(x1.area(), x2.area(), 12)
        self.assertEqual(x3.area(), 24)

    def test_str(self):
        x1 = Rectangle(2, 3, 5, 6, 10)
        self.assertEqual(str(x1), "[Rectangle] (10) 5/6 - 2/3")

    def test_str_Aftr_update(self):
        x1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(x1), "[Rectangle] (1) 1/1 - 1/1")
        x1.update(17, 2, 5, 6, 7)
        self.assertEqual(str(x1), "[Rectangle] (17) 6/7 - 2/5")

    def test_print(self):
        x1 = Rectangle(17, 2, 5, 6, 7)
        out = StringIO()
        sys.stdout = out
        print(x1)
        self.assertEqual(out.getvalue(),
                         "[Rectangle] (7) 5/6 - 17/2\n")
        
    def test_print_Aftr_update(self):
        x1 = Rectangle(17, 2, 5, 6, 7)
        x1.update(18, 4, 3, 0, 5)
        out = StringIO()
        sys.stdout = out
        print(x1)
        self.assertEqual(out.getvalue(),
                         "[Rectangle] (18) 0/5 - 4/3\n")

    def test_display(self):
        x1 = Rectangle(2, 3)

        out = StringIO()
        sys.stdout = out
        x1.display()
        x = "##\n##\n##\n"
        self.assertEqual(out.getvalue(), x)

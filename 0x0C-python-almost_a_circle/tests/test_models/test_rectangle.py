#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_ids(self):
        x1 = Rectangle(1 , 2)
        x2 = Rectangle(1 , 2)
        x3 = Rectangle(1 , 2, 3, 4 , 5)
        self.assertEqual(x1.id , x2.id - 1)
        self.assertEqual(x2.id , x1.id + 1)

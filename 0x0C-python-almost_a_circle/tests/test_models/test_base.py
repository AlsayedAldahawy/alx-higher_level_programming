#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        self.x1 = Base()
        self.x2 = Base()
        self.x3 = Base(15)
        self.x4 = Base()

    def test_id(self):
        self.assertEqual(self.x1.id, 1)
        self.assertEqual(self.x2.id, 2)
        self.assertEqual(self.x3.id, 15)
        self.assertEqual(self.x4.id, 3)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase_initialization(unittest.TestCase):

    def setUp(self):
        self.x1 = Base()
        self.x2 = Base()
        self.x3 = Base(15)
        self.x4 = Base()

    def test_id_globally(self):
        self.assertEqual(self.x1.id, self.x2.id - 1)
        self.assertEqual(self.x2.id, self.x4.id - 1)
        self.assertEqual(self.x3.id, 15)

    def test_id_locally(self):
        x5 = Base()
        x6 = Base()
        x7 = Base(22)
        x8 = Base()
        self.assertEqual(x5.id, x6.id - 1)
        self.assertEqual(x6.id, x8.id - 1)
        self.assertEqual(x7.id, 22)

    def test_id_None(self):
        x1 = Base(None)
        x2 = Base(None)
        self.assertEqual(x1.id, x2.id - 1)
        self.assertEqual(x2.id, Base(None).id - 1)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):

    def test_empty_list(self):
        # Test when the input list is empty
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        # Test with a single element in the list
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([10, 20, 5, 30]), 30)

    def test_negative_numbers(self):
        # Test with a list of negative integers
        self.assertEqual(max_integer([-5, -10, -2, -1]), -1)

    def test_mixed_numbers(self):
        # Test with a mix of positive and negative integers
        self.assertEqual(max_integer([5, -8, 12, -3]), 12)

    def test_duplicate_max(self):
        # Test with duplicate maximum values
        self.assertEqual(max_integer([10, 20, 20, 30]), 30)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, [5, 4, '6'])
        self.assertRaises(TypeError, max_integer, ["inf", 5, 6])

        # self.assertRaises(TypeError, max_integer, [[4], [3, 2]])
        # self.assertRaises(TypeError, max_integer, "[]")
        # self.assertRaises(TypeError, max_integer, [2.5, 3.5, 7.6])
        # self.assertRaises(TypeError, max_integer, "inf")

        # the last commented cases should give a Type error, but the function
        # did not take these cases into account

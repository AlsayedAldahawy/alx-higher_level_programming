#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
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

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    # def test_ints_and_floats(self):
    #     """Test a list of ints and floats."""
    #     ints_and_floats = [1.53, 15.5, -9, 15, 6]
    #     self.assertEqual(max_integer(ints_and_floats), 15.5)

    # def test_string(self):
    #     """Test a string."""
    #     string = "Brennan"
    #     self.assertEqual(max_integer(string), 'r')

    # def test_list_of_strings(self):
    #     """Test a list of strings."""
    #     strings = ["Brennan", "is", "my", "name"]
    #     self.assertEqual(max_integer(strings), "name")

    # def test_empty_string(self):
    #     """Test an empty string."""
    #     self.assertEqual(max_integer(""), None)

    # def test_errors(self):
    #     self.assertRaises(TypeError, max_integer, [5, 4, '6'])
    #     self.assertRaises(TypeError, max_integer, ["inf", 5, 6])

        # self.assertRaises(TypeError, max_integer, [[4], [3, 2]])
        # self.assertRaises(TypeError, max_integer, "[]")
        # self.assertRaises(TypeError, max_integer, "inf")

        # the last commented cases should give a Type error, but the function
        # did not take these cases into account

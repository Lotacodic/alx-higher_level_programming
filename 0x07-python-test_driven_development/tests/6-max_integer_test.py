#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [4, 3, 1, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning maximum value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test a list with only a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of integers and floats."""
        ints_and_floats = [2.33, 15.66, -9, 6, 15, -22.9]
        self.assertEqual(max_integer(ints_and_floats), 15.66)

    def test_strings(self):
        """Test a list of strings."""
        strings = ["Omotayo", "is", "my", "first", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_string(self):
        """Test a string."""
        string = "Omotayo"
        self.assertEqual(max_integer(string), 'y')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

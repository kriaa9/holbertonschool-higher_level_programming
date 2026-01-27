#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function"""

    def test_regular_list(self):
        """Test with a standard ordered list of integers"""
        l = [1, 2, 3, 4]
        result = max_integer(l)
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        l = [1, 3, 4, 2]
        result = max_integer(l)
        self.assertEqual(result, 4)

    def test_max_at_beginning(self):
        """Test with a list where max is at the beginning"""
        l = [4, 3, 2, 1]
        result = max_integer(l)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list"""
        l = []
        result = max_integer(l)
        self.assertIsNone(result)

    def test_one_element(self):
        """Test with a list containing only one integer"""
        l = [7]
        result = max_integer(l)
        self.assertEqual(result, 7)

    def test_floats(self):
        """Test with a list of floats"""
        l = [1.53, 6.33, -9.123, 15.2, 6.0]
        result = max_integer(l)
        self.assertEqual(result, 15.2)

    def test_ints_and_floats(self):
        """Test with a list of mixed ints and floats"""
        l = [1.53, 15.5, -9, 15, 6]
        result = max_integer(l)
        self.assertEqual(result, 15.5)

    def test_string(self):
        """Test with a string"""
        string = "Brennan"
        result = max_integer(string)
        self.assertEqual(result, 'r')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        l = ["Brennan", "Louis", "Hello"]
        result = max_integer(l)
        self.assertEqual(result, "Louis")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(max_integer(""))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        l = [-5, -2, -3, -4]
        result = max_integer(l)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_sorted_list(self):
        """Test already sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted_list(self):
        """Test reverse sorted list"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_identical_numbers(self):
        """Test list with identical numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

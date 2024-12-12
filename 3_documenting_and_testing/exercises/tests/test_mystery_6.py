import unittest

from ..mystery_6 import mystery_6


class TestMystery6(unittest.TestCase):
    """Test the mystery_6 function"""

    def test_0(self):
        """It should evaluate a positive input and create a list with 2 numbers"""
        actual = mystery_6(2, 10)
        expected = [10, 11]
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate a list with 0 elements"""
        actual = mystery_6(0, 10)
        expected = []
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate a list with negative number"""
        actual = mystery_6(3, -1)
        expected = [-1, 0, 1]
        self.assertEqual(actual, expected)

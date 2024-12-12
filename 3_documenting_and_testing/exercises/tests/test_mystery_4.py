import unittest

from ..mystery_4 import mystery_4


class TestMystery4(unittest.TestCase):
    """Test the mystery_4 function"""

    def test_0(self):
        """It should evaluate a positive input"""
        actual = mystery_4(4)
        expected = [0, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate a zero as an input"""
        actual = mystery_4(0)
        expected = []
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate a negative input"""
        actual = mystery_4(-1)
        expected = []
        self.assertEqual(actual, expected)

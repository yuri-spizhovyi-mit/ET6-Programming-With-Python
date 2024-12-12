import unittest

from ..mystery_5 import mystery_5


class TestMystery5(unittest.TestCase):
    """Test the mystery_5 function"""

    def test_0(self):
        """It should evaluate a list of positive numbers and create b list"""
        actual = mystery_5([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_1(self):
        """ "It should evaluate a list included negative number"""
        actual = mystery_5([3, 2, -1])
        expected = [-1, 2, 3]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate a list rearragned and appended to existing list"""
        actual = mystery_5([5, 4], [3, 2, 1])
        expected = [3, 2, 1, 4, 5]
        self.assertEqual(actual, expected)

import unittest

from ..mystery_9 import mystery_9


class TestMystery9(unittest.TestCase):
    """Test mystery_9 function"""

    def test_0(self):
        """It should evaluate sorting of empty list"""
        actual = mystery_9([])
        expected = []
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate sorting of a list with positive
        negative numbers and zero"""
        actual = mystery_9([0, 100, -100])
        expected = [-100, 0, 100]
        self.assertEqual(actual, expected)

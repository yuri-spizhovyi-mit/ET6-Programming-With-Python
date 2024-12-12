import unittest

from ..mystery_8 import mystery_8


class TestMystery8(unittest.TestCase):
    """Test mystery_8 function"""

    def test_0(self):
        """It should evaluate filtering of empty list"""
        actual = mystery_8([], "banana")
        expected = []
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate filtering by empty string"""
        actual = mystery_8(["apple", "banana", "banana"], "")
        expected = ["apple", "banana", "banana"]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate filtering by absent word"""
        actual = mystery_8(["apple", "banana", "banana"], "pear")
        expected = []
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should evaluate filtering by search word"""
        actual = mystery_8(["apple", "banana", "banana"], "banana")
        expected = ["banana", "banana"]
        self.assertEqual(actual, expected)

    def test_4(self):
        """It should evaluate a search by part of search word"""
        actual = mystery_8(["apple", "applepie", "banana"], "apple")
        expected = ["apple", "applepie"]
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should evaluate filtering by search char"""
        actual = mystery_8(["apple", "banana", "grape"], "a")
        expected = ["apple", "banana", "grape"]
        self.assertEqual(actual, expected)

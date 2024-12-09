import unittest

from ..mystery_2 import mystery_2


class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function"""

    def test_0(self):
        """It should evaluate an empty string"""
        actual = mystery_2("")
        expected = None
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate a string with length equal 1"""
        actual = mystery_2("a")
        expected = 1
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate a string with the lenght more than 1"""
        actual = mystery_2("ab")
        expected = 2
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should raise a TypeError when an integer is passed as input"""
        with self.assertRaises(TypeError):
            mystery_2(1)

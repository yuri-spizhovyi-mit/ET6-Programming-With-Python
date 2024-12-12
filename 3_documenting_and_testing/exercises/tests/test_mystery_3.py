import unittest

from ..mystery_3 import mystery_3


class TestMystery3(unittest.TestCase):
    """Test the mystery_3 function"""

    def test_1(self):
        actual = mystery_3(1, 2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = mystery_3(3, 2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = mystery_3(3, 3)
        expected = 6
        self.assertEqual(actual, expected)

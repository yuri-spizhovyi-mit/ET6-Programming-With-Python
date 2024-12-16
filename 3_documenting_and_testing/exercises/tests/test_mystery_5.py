import unittest
from ..mystery_5 import mystery_5


class TestMystery5(unittest.TestCase):
    """Test the mystery_5 function"""

    def test_positive_numbers(self):
        """It should evaluate a list of positive numbers and create b list"""
        actual = mystery_5([3, 2, 1])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """It should evaluate a list containing a negative number"""
        actual = mystery_5([3, 2, -1])
        expected = [-1, 2, 3]
        self.assertEqual(actual, expected)

    def test_append_to_existing(self):
        """It should evaluate a list rearranged and appended to an existing list"""
        actual = mystery_5([5, 4], [3, 2, 1])
        expected = [3, 2, 1, 4, 5]
        self.assertEqual(actual, expected)

    def test_special_chars_only(self):
        """It should handle a list with only special characters"""
        actual = mystery_5(['!', '@', '#'])
        expected = ['!', '#', '@']
        self.assertEqual(actual, expected)

    def test_incompatible_types(self):
        """It should raise a TypeError for mixed types in the input"""
        with self.assertRaises(TypeError):
            mystery_5(['Z', 'a', 5, 2])

    def test_empty_lists(self):
        """It should handle empty input lists for a and b"""
        actual = mystery_5([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_empty_a_with_non_empty_b(self):
        """It should append nothing when a is empty and b is provided"""
        actual = mystery_5([], ['!@#', 'xyz'])
        expected = ['!@#', 'xyz']
        self.assertEqual(actual, expected)

    def test_type_error_mixed(self):
        """It should raise a TypeError for incompatible types in a"""
        with self.assertRaises(TypeError):
            mystery_5(['-3', -1, '0', 3])

    def test_large_numbers(self):
        """It should handle large numbers in the input list"""
        actual = mystery_5([10**6, -10**6, 0])
        expected = [-1000000, 0, 1000000]
        self.assertEqual(actual, expected)

    def test_empty_a_and_none_b(self):
        """It should return an empty list when a is empty and b is None"""
        actual = mystery_5([], None)
        expected = []
        self.assertEqual(actual, expected)

    def test_a_none_b_none(self):
        """It should return a sorted list when both a and b are provided"""
        actual = mystery_5([3, 2, 1], None)
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_mixed_strings(self):
        """It should handle strings with special characters"""
        actual = mystery_5(['abc', 'xyz', '123', '!@#'])
        expected = ['!@#', '123', 'abc', 'xyz']
        self.assertEqual(actual, expected)

    def test_single_special_char(self):
        """It should handle a single special character in a"""
        actual = mystery_5(['!'])
        expected = ['!']
        self.assertEqual(actual, expected)

    def test_single_element(self):
        """It should handle a single element in the input list"""
        actual = mystery_5([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_duplicates_in_a(self):
        """It should handle duplicate elements in the input list"""
        actual = mystery_5([2, 2, 1, 1])
        expected = [1, 1, 2, 2]
        self.assertEqual(actual, expected)

    def test_type_error_in_b(self):
        """It should raise a TypeError if b contains an incompatible type"""
        with self.assertRaises(TypeError):
            mystery_5([1, 2, 3], ['a', 5])

    def test_empty_a_nonempty_b_valid(self):
        """It should sort b if a is empty"""
        actual = mystery_5([], [3, 1, 2])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)


    def test_empty_b_nonempty_a_valid(self):
        """It should merge a valid non-empty a with an empty b"""
        actual = mystery_5([3, 1, 2], [])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

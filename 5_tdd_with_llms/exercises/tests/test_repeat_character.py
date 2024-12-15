#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the repeat_character function.

Created on 2024-12-13

@author: Yurii Spizhovyi + ChatGPT
"""

import unittest
from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    # Basic functionality
    def test_single_occurrence(self):
        """It should be a one repetition of character"""
        self.assertEqual(repeat_character("hello", "e", 1), "hello")

    def test_multiple_occurrences(self):
        """It should correctly repeat the character multiple times"""
        self.assertEqual(repeat_character("hello", "e", 2), "heello")

    def test_character_not_in_string(self):
        """It should return the original string if the character is not present"""
        self.assertEqual(repeat_character("hello", "x", 3), "hello")

    def test_empty_string(self):
        """It should handle an empty string without errors"""
        self.assertEqual(repeat_character("", "e", 1), "")

    def test_no_repetition(self):
        """It should remove the character from the string if repetition is zero"""
        self.assertEqual(repeat_character("hello", "l", 0), "heo")

    def test_large_repetition(self):
        """It should handle large repetition counts for the character"""
        self.assertEqual(repeat_character("abc", "b", 5), "abbbbbc")

    # Edge cases
    def test_special_characters(self):
        """It should repeat special characters correctly"""
        self.assertEqual(repeat_character("a!b!c!", "!", 3), "a!!!b!!!c!!!")

    def test_numeric_characters(self):
        """It should handle numeric characters in the string"""
        self.assertEqual(repeat_character("123", "2", 2), "1223")

    # Defensive assertions
    def test_non_string_item(self):
        """It should raise a TypeError when the input is not a string"""
        with self.assertRaises(TypeError):
            repeat_character(123, "e", 1)

    def test_non_string_char(self):
        """It should raise a TypeError when the character is not a string"""
        with self.assertRaises(TypeError):
            repeat_character("hello", 5, 1)

    def test_non_integer_num(self):
        """It should raise a TypeError when the repetition count is not an integer"""
        with self.assertRaises(TypeError):
            repeat_character("hello", "e", "two")

    def test_char_not_single_character(self):
        """It should raise a ValueError when the character is not a single character"""
        with self.assertRaises(ValueError):
            repeat_character("hello", "el", 1)

    def test_negative_repetition(self):
        """It should raise a ValueError when the repetition count is negative"""
        with self.assertRaises(ValueError):
            repeat_character("hello", "e", -1)

if __name__ == "__main__":
    unittest.main()

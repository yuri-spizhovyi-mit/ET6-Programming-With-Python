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
        self.assertEqual(repeat_character("hello", "e", 1), "hello")

    def test_multiple_occurrences(self):
        self.assertEqual(repeat_character("hello", "e", 2), "heello")

    def test_character_not_in_string(self):
        self.assertEqual(repeat_character("hello", "x", 3), "hello")

    def test_empty_string(self):
        self.assertEqual(repeat_character("", "e", 1), "")

    def test_no_repetition(self):
        self.assertEqual(repeat_character("hello", "l", 0), "heo")

    def test_large_repetition(self):
        self.assertEqual(repeat_character("abc", "b", 5), "abbbbbc")

    # Edge cases
    def test_special_characters(self):
        self.assertEqual(repeat_character("a!b!c!", "!", 3), "a!!!b!!!c!!!")

    def test_numeric_characters(self):
        self.assertEqual(repeat_character("123", "2", 2), "1223")

    # Defensive assertions
    def test_non_string_item(self):
        with self.assertRaises(TypeError):
            repeat_character(123, "e", 1)

    def test_non_string_char(self):
        with self.assertRaises(TypeError):
            repeat_character("hello", 5, 1)

    def test_non_integer_num(self):
        with self.assertRaises(TypeError):
            repeat_character("hello", "e", "two")

    def test_char_not_single_character(self):
        with self.assertRaises(ValueError):
            repeat_character("hello", "el", 1)

    def test_negative_repetition(self):
        with self.assertRaises(ValueError):
            repeat_character("hello", "e", -1)

if __name__ == "__main__":
    unittest.main()

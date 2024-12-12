#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-12

@author: Yurii Spizhovyi + Chat GPT
"""

import unittest
from ..exclusive_or import exclusive_or

class TestExclusiveOr(unittest.TestCase):
    def test_item_in_first_list_only(self):
        self.assertTrue(exclusive_or("hello", ["hello"], ["world"]))

    def test_item_in_second_list_only(self):
        self.assertTrue(exclusive_or("hello", ["world"], ["hello"]))

    def test_item_in_both_lists(self):
        self.assertFalse(exclusive_or("hello", ["hello"], ["hello"]))

    def test_item_not_in_either_list(self):
        self.assertFalse(exclusive_or("hello", ["world"], ["planet"]))

    def test_empty_item_in_first_list_only(self):
        self.assertTrue(exclusive_or("", [""], ["world"]))

    def test_empty_item_in_second_list_only(self):
        self.assertTrue(exclusive_or("", ["world"], [""]))

    def test_empty_item_in_both_lists(self):
        self.assertFalse(exclusive_or("", [""], [""]))

    def test_empty_item_not_in_either_list(self):
        self.assertFalse(exclusive_or("", ["planet"], ["galaxy"]))

    def test_case_sensitive_match_in_first_list(self):
        self.assertTrue(exclusive_or("Hello", ["Hello"], ["hello"]))

    def test_case_sensitive_match_in_second_list(self):
        self.assertTrue(exclusive_or("Hello", ["hello"], ["Hello"]))

    def test_special_characters_in_first_list(self):
        self.assertTrue(exclusive_or("Hello, world!", ["Hello, world!"], ["Hello"]))

    def test_special_characters_in_second_list(self):
        self.assertTrue(exclusive_or("Hello, world!", ["Hello"], ["Hello, world!"]))

    def test_item_with_space_in_first_list_only(self):
        self.assertTrue(exclusive_or("hello world", ["hello world"], [""]))

    def test_item_with_space_in_second_list_only(self):
        self.assertTrue(exclusive_or("hello world", [""], ["hello world"]))

    def test_item_with_space_in_both_lists(self):
        self.assertFalse(exclusive_or("hello world", ["hello world"], ["hello world"]))

    def test_item_with_partial_match_in_lists(self):
        self.assertFalse(exclusive_or("hello", ["helloworld"], ["world"]))

    def test_non_string_items(self):
        with self.assertRaises(TypeError):
            exclusive_or(123, ["123"], ["world"])

    def test_first_list_is_none(self):
        with self.assertRaises(TypeError):
            exclusive_or("hello", None, ["world"])

    def test_second_list_is_none(self):
        with self.assertRaises(TypeError):
            exclusive_or("hello", ["hello"], None)

    def test_item_is_none(self):
        with self.assertRaises(TypeError):
            exclusive_or(None, ["hello"], ["world"])

    def test_first_list_is_empty(self):
        self.assertTrue(exclusive_or("hello", [], ["hello"]))

    def test_second_list_is_empty(self):
        self.assertTrue(exclusive_or("hello", ["hello"], []))

    def test_both_lists_are_empty(self):
        self.assertFalse(exclusive_or("hello", [], []))

    def test_lists_with_nested_lists(self):
        with self.assertRaises(TypeError):
            exclusive_or("hello", [["hello"]], ["world"])

if __name__ == "__main__":
    unittest.main()

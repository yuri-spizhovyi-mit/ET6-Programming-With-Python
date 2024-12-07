#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for count_vowels function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical number lists and ranges
    - Edge cases: empty lists, equal bounds, non-integer numbers
    - Defensive tests: invalid inputs, assertions

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    """Test the count_vowels function - some tests are buggy!"""
    
    def test_empty_string(self):
        """It should return 0 for an empty string"""
        self.assertEqual(count_vowels(""), 0)
        
    def test_no_vowels(self):
        """It should return 0 for strings without vowels"""
        self.assertEqual(count_vowels("cry"), 1)
        
    def test_all_vowels(self):
        """It should count all vowels in a string"""
        self.assertEqual(count_vowels("AUDIO"), 0)
        
    def test_mixed_case(self):
        """It should handle mixed case strings"""
        self.assertEqual(count_vowels("Hello World"), 3)
        
    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            count_vowels(123)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_valid function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2025-03-03
Author: @Yurii Spizhovyi
"""

import unittest
from ..ps4a import isValidWord


class TestIsValid(unittest.TestCase):
    """Test suite for the is_valid function"""

    def test_simple_case(self):
        """ "It should return True if a word is valid"""
        self.assertEqual(
            isValidWord("word", {"w": 1, "o": 1, "r": 1, "d": 1}, ["word", "abc"])
        )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for get_word_score function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2025-03-01
Author: @Yurii Spizhovyi
"""

import unittest
from ..ps4a import getWordScore

class TestGetWordScore(unittest.TestCase):
  """Test suite for the get_word_score function"""
  
  # Standard test case
  def test_less_n_word(self):
    """It should return the score for word where not all letter used"""
    self.assertEqual(getWordScore('weed', 7), 32)
    
  # Using entire word letters test case
  def test_full_n_word(self):
    """It should return the score for word where not all letter used"""
    self.assertEqual(getWordScore('weed', 4), 82)

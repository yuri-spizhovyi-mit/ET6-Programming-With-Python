#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for update_hand function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2025-03-02
Author: @Yurii Spizhovyi
"""

import unittest
from ..ps4a import updateHand


class TestUpdateHand(unittest.TestCase):
  """Test suite for the get_word_score function"""
  def test_simple_case(self):
    """It should return a dictionary without letters in a word"""
    self.assertEqual(updateHand({'a': 2}, 'aa'), {'a': 0})

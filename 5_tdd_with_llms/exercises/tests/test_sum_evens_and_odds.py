#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_evens_and_odds function.

Created on 2024-12-13

@author: Yurii Spizhovyi + ChatGPT
"""

import unittest
from ..sum_evens_and_odds import sum_evens_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    # Basic functionality
    def test_basic_case(self):
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4]), {"evens": 6, "odds": 4})

    # Edge cases
    def test_empty_list(self):
        self.assertEqual(sum_evens_and_odds([]), {"evens": 0, "odds": 0})

    def test_all_even_numbers(self):
        self.assertEqual(sum_evens_and_odds([2, 4, 6, 8]), {"evens": 20, "odds": 0})

    def test_all_odd_numbers(self):
        self.assertEqual(sum_evens_and_odds([1, 3, 5, 7]), {"evens": 0, "odds": 16})

    def test_single_even_number(self):
        self.assertEqual(sum_evens_and_odds([2]), {"evens": 2, "odds": 0})

    def test_single_odd_number(self):
        self.assertEqual(sum_evens_and_odds([1]), {"evens": 0, "odds": 1})

    # Mixed positive and negative numbers
    def test_mixed_positive_and_negative(self):
        self.assertEqual(sum_evens_and_odds([-2, -3, 4, 5]), {"evens": 2, "odds": 2})

    def test_all_negative_numbers(self):
        self.assertEqual(
            sum_evens_and_odds([-2, -4, -5, -7]), {"evens": -6, "odds": -12}
        )

    # Mixed integers and zeros
    def test_including_zero(self):
        self.assertEqual(sum_evens_and_odds([0, 1, 2, 3]), {"evens": 2, "odds": 4})

    def test_all_zeros(self):
        self.assertEqual(sum_evens_and_odds([0, 0, 0]), {"evens": 0, "odds": 0})

    # Large input
    def test_large_input(self):
        large_list = [i for i in range(1, 10001)]  # Numbers from 1 to 10,000
        self.assertEqual(
            sum_evens_and_odds(large_list), {"evens": 25005000, "odds": 25000000}
        )

    # Defensive assertions
    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            sum_evens_and_odds([1, 2, "three", 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_evens_and_odds("not a list")

    def test_nested_lists(self):
        with self.assertRaises(TypeError):
            sum_evens_and_odds([1, [2, 3], 4])


if __name__ == "__main__":
    unittest.main()

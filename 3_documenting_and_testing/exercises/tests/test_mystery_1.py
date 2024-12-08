"""
Created on 2024-12-08
    
@author: Yurii Spizhovyi
"""

import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """Test the  mystery_1 function"""
    
    def test_0(self):
        """It should evaluate 1 and 2 to 3"""
        actual = mystery_1(1, 2)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate -1 and -1 to -2"""
        actual = mystery_1(-1, -1)
        expected = -2
        self.assertEqual(actual, expected)
        
    def test_3(self):
        """It should evaluate -1 and 1 to 0"""
        actual = mystery_1(-1, 1)
        expected = 0
        self.assertEqual(actual, expected)

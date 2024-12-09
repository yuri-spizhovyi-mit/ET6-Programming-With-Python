import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ Test the mystery_7 function"""
    
    def test_0(self):
        """It should evaluate an input with the empty output"""
        actual = mystery_7(["one", "two", "three"], "four")
        expected = []
        self.assertEqual(actual, expected)
        
    def test_1(self):
        """It should evaluate an input with the output including full words"""
        actual = mystery_7(["one", "two", "three", "one hundred"], "one")
        expected = ['one', 'one hundred']
        self.assertEqual(actual, expected)
        
    def test_2(self):
        """It should evaluate an output based by part of the word input"""   
        actual = mystery_7(["one", "stone", "alone", "money", "two"], "one")
        expected = ['one', 'stone', 'alone', 'money']
        self.assertEqual(actual, expected)
        
    def test_3(self):
        """It should evaluate a filtering based on special characters"""
        actual = mystery_7(["@one", "#stone", "!alone", "money", "two"], "#")
        expected = ['#stone']
        self.assertEqual(actual, expected)
    

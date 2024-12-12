#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-12

@author: Yurii Spizhovyi + Chat GPT
"""


def exclusive_or(item, first, second):
    """Exclusive Or

    Write a function that takes in a string and two lists of strings. 
    It will return true if the item is in _only one_ of the lists.

    Args:
        item (str): The string to search for in the two lists.
        first (list[str]): The first list of strings.
        second (list[str]): The second list of strings.

    Raises:
        TypeError: If `item` is not a string.
        TypeError: If `first` is not a list.
        TypeError: If `second` is not a list.
        TypeError: If elements of `first` or `second` are not strings.

    Returns:
        bool: True if the 'item' is only in list 'first' or is only in list 'second'.
              False if the 'item' is in both lists at the same time or does not exist in either list.

    Examples:
        >>> exclusive_or("hello", ["hello"], ["world"])
        True

        >>> exclusive_or("hello", ["hello world"], ["world"])
        True

        >>> exclusive_or("hello", ["world"], ["hello"])
        True

        >>> exclusive_or("hello", ["world"], ["hello world"])
        True

        >>> exclusive_or("hello", [""], ["hello world"])
        True

        >>> exclusive_or("hello", ["hello world"], [""])
        True

        >>> exclusive_or("", [""], ["hello world"])
        True

        >>> exclusive_or("", ["hello world"], [""])
        True

        >>> exclusive_or("hello world", ["hello world"], [""])
        True

        >>> exclusive_or("Hello, world!", ["Hello, world!"], ["Hello"])
        True

        >>> exclusive_or("hello", ["hello"], ["hello"])
        False

        >>> exclusive_or("hello", [""], [""])
        False

        >>> exclusive_or("Hello, world!", ["Hello, world!"], ["Hello, world!"])
        False

        >>> exclusive_or("hello", ["helloworld"], ["world"])
        False

        >>> exclusive_or("hello", [], ["hello"])
        True

        >>> exclusive_or("hello", ["hello"], [])
        True

        >>> exclusive_or("hello", [], [])
        False

        >>> exclusive_or("", [""], [""])
        False

        >>> exclusive_or("", [], [""])
        True

        >>> exclusive_or("", [""], [])
        True

        >>> exclusive_or("", [], [])
        False

        >>> exclusive_or("Hello", ["Hello"], ["hello"])
        True

        >>> exclusive_or("Hello", ["hello"], ["Hello"])
        True

        >>> exclusive_or("Hello, world!", ["Hello, world!"], ["Hello"])
        True

        >>> exclusive_or("Hello, world!", ["Hello"], ["Hello, world!"])
        True

        >>> exclusive_or("world", ["Hello, world!"], ["world"])
        True

        >>> exclusive_or("world", ["Hello, world!"], ["Hello, world!"])
        False

    """
    if not isinstance(item, str):
        raise TypeError("item must be a string")
    if not isinstance(first, list) or not isinstance(second, list):
        raise TypeError("first and second must be lists")
    if not all(isinstance(element, str) for element in first):
        raise TypeError("All elements in first must be strings")
    if not all(isinstance(element, str) for element in second):
        raise TypeError("All elements in second must be strings")

    in_first = item in first
    in_second = item in second

    return (in_first or in_second) and not (in_first and in_second)

"""Exclusive Or

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _only one_ of the lists.

Parameters:
item: str
first: list[str]
second: list[str]

Returns: True if the 'item' is only in list 'first' or is only in list 'second'
        False if the 'item' in both lists at the same time or does not exists in lists at all


"""


def exclusive_or():
    """
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

    """
    pass

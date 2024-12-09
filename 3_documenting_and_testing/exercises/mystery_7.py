"""
Created on 2024-12-08

@author: Yurii Spizhovyi
"""


def mystery_7(a: list[str], b: str) -> list[str]:
    """Finds elements in the input list and returns the list of these elements

    Parameters:
    a: list[str] a list of strings values
    b: str a string value

    Returns -> list[str] a list with elements from list a that contains a value b


    >>> mystery_7(["one", "two", "three"], "four")
    []

    >>> mystery_7(["one", "two", "three", "one hundred"], "one")
    ['one', 'one hundred']

    >>> mystery_7(["one", "stone", "alone", "money", "two"], "one")
    ['one', 'stone', 'alone', 'money']

    >>> mystery_7(["@one", "#stone", "!alone", "money", "two"], "#")
    ['#stone']
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c

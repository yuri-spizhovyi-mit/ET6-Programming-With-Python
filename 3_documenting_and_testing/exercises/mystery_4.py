"""
Created on 2024-12-08

@author: Yurii Spizhovi
"""


def mystery_4(a: int) -> list[int]:
    """Create a list of numbers based on provided number

    Parameters:

    Returns -> list [] of integers

    >>> mystery_4(4)
    [0, 1, 2, 3]

    >>> mystery_4(0)
    []

    >>> mystery_4(-4)
    []
    """

    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b

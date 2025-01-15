"""
Created on 2024-12-08

@author: Yurii Spizhovyi
"""

from typing import Optional


def mystery_2(a: str) -> Optional[int]:
    """Returns a length of string

    Parameters:
        a string: str, greater than or equal to zero
    Returns -> int greater or equals zero or None

    >>> print(mystery_2(""))
    None

    >>> mystery_2("a")
    1

    >>> mystery_2("ab")
    2

    >>> mystery_2(1) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: object of type 'int' has no len()
    """
    if len(a) == 0:
        return None

    return len(a)


mystery_2("")

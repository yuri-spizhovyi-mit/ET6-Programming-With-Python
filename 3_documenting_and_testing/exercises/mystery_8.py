"""
Created on 2024-12-08

@author: Yurii Spizhovyi
"""


def mystery_8(a: list[str], b: str) -> list[str]:
    """Function filters by parameter b from the list a

    Args:
        a (_type_): list[str] a list of strings
        b (_type_): str a search word

    Returns:
        _type_: a list of filtered elements
        
    >>> mystery_8([], "banana")
    []
    
    >>> mystery_8(["apple", "banana", "banana"], "")
    ['apple', 'banana', 'banana']
    
    >>> mystery_8(["apple", "banana", "banana"], "pear")
    []
    
    >>> mystery_8(["apple", "banana", "banana"], "banana")
    ['banana', 'banana']
    
    >>> mystery_8(["apple", "applepie", "banana"], "apple")
    ['apple', 'applepie']
    
    >>> mystery_8(["apple", "banana", "grape"], "a")
    ['apple', 'banana', 'grape']
    
    """
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c

mystery_8(["apple", "banana", "banana"], "banana")

"""
Created on 2024-12-08

@author: Yurii Spizhovi
"""

def mystery_3(a: int, b: int) -> int:
    """Compare 2 numbers and return one of them or their sum depending of the conditions
    
    Parameters:
    
    Returns -> int a if a<b, b if a > b or their sum if a===b
    
    >>> mystery_3(1, 2)
    1
    
    >>> mystery_3(3, 2)
    2
    
    >>> mystery_3(3, 3)
    6
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b

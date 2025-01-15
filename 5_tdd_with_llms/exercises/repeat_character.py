"""Repeat Character

Write a function that takes in a string, a single character, and a number.
The function returns a string with each occurrence of the character repeated n times.

"""


def repeat_character(item: str, char: str, num: int) -> str:
    """
    Repeat Character

    This function takes a string, a single character, and a number, and returns a string
    where each occurrence of the character is repeated `num` times.

    Args:
        item (str): The input string to modify.
        char (str): The character to search for and repeat.
        num (int): The number of times to repeat each occurrence of the character.

    Raises:
        TypeError: If `item` is not a string.
        TypeError: If `char` is not a string.
        TypeError: If `num` is not an integer.
        ValueError: If `char` is not a single character.
        ValueError: If `num` is negative.

    Returns:
        str: The modified string with repeated characters.

    Examples:
        >>> repeat_character("hello", "e", 1)
        'hello'

        >>> repeat_character("hello", "e", 2)
        'heello'

        >>> repeat_character("hello melon", "e", 2)
        'heello meelon'

        >>> repeat_character("hello wello", "x", 3)
        'hello melon'

        >>> repeat_character("", "e", 1)
        ''

        >>> repeat_character("hello", "l", 0)
        'heo'

        >>> repeat_character("hello", "l", 3)
        'hellllo'

        >>> repeat_character("hello", 5, 2)
        Traceback (most recent call last):
        TypeError: char must be a string

        >>> repeat_character("hello", "l", -1)
        Traceback (most recent call last):
        ValueError: num must be non-negative
    """
    if not isinstance(item, str):
        raise TypeError("item must be a string")
    if not isinstance(char, str):
        raise TypeError("char must be a string")
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    if len(char) > 1:
        raise ValueError("char must be a single character")
    if num < 0:
        raise ValueError("num must be non-negative")

    # Modify the string by repeating the character
    result = []
    for c in item:
        if c == char:
            result.append(c * num)
        else:
            result.append(c)

    return "".join(result)

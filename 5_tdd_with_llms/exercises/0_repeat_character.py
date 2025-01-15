"""Repeat Character

Write a function that takes in a string, a single character, and a number.
The function returns a string with each occurrence of the character repeated n times.

"""


def repeat_character(item: str, char, str, num: int) -> str:
    """Args:
        item (str): The string of characters, words, etc.
        char (str): The character to search in a string.
        num (int): The number of occurrences of the character in a string

    Raises:
        TypeError: If `item` is not a string.
        TypeError: If `char` is not a string.
        TypeError: If `num` is not an integer.

    Returns:
        str: a string with the number of `char` occurrences `num` times

    Examples:
        >>> repeat_character("hello", "e", 1)
        "hello"

        >>> repeat_character("hello melon", "e", 1)
        "hello"

        >>> repeat_character("hello melon", "e", 2)
        "hello melon"

        >>> repeat_character("hello melon", "a", 1)
        ""
        >>> repeat_character("hello melon", "e", 3)
        ""
        >>> repeat_character("", "e", 1)
        ""

        >>> repeat_character("", "e", 1)
        ""

        >>> repeat_character(1, "e", 1)
        TypeError

        >>> repeat_character("hello", 1, 1)
        TypeError

        >>> repeat_character("hello", 1, "one")
        TypeError

        >>> repeat_character("", "e", "")
        # I guess this should be error

    """

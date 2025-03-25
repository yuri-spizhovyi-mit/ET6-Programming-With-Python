def sum_digits(s):
    """assumes s a string
      Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception.

    Input: string

    Return: sum of digits in the string
    If there is no digits - raise a ValueError exception"""
    # Your code here
    result = 0
    count = 0
    for char in s:
        if char.isdigit():
            result += int(char)
            count += 1
    if count == 0:
        raise ValueError("There is no digits in the string")
    return result


# print(sum_digits("a;35d4"))
print(sum_digits("a;d0"))

# Separate letters and numbers from a string, then separate letters by case and count them.

s = "aabA123"


def separator(s):
    letters = sum(1 for char in s if char.isalpha())
    lower = sum(1 for char in s if char.islower())
    upper = sum(1 for char in s if char.isupper())
    return (
        f"Number of lowercase letters is {lower}, uppercase is {upper}, total {letters}"
    )


print(separator(s))

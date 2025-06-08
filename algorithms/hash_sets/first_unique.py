def first_unique(s: str):
    # First pass: count each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

        # Second pass: find the first character with count 1

    for char in s:
        if char_count[char] == 1:
            return char
    return "_"


print(first_unique("leetcode"))  # ➞ "l"
print(first_unique("loveleetcode"))  # ➞ "v"
print(first_unique("aabbcc"))  # ➞ "_"

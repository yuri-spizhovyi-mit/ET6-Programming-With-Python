from collections import OrderedDict


def first_unique_one_pass(s: str) -> str:
    seen = OrderedDict()

    for i, char in enumerate(s):
        if char in seen:
            seen[char] = (seen[char][0] + 1, seen[char][1])  # increment count
        else:
            seen[char] = (1, i)  # (count, index)

    for char, (count, index) in seen.items():
        if count == 1:
            return char

    return "_"


print(first_unique_one_pass("leetcode"))  # ➞ "l"
print(first_unique_one_pass("loveleetcode"))  # ➞ "v"
print(first_unique_one_pass("aabbcc"))  # ➞ "_"

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Count characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Subtract counts using characters in t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

print(is_anagram("listen", "silent"))   # True
print(is_anagram("rat", "car"))         # False
print(is_anagram("aacc", "ccac"))       # False


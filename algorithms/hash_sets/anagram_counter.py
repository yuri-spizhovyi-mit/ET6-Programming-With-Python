from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))  # False
print(is_anagram("aacc", "ccac"))  # False
print(is_anagram("hello", "world"))  # False
print(is_anagram("debit card", "bad credit"))  # True

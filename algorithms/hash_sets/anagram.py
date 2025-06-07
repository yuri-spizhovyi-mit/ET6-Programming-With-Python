def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # from a to z

    for cs, ct in zip(s, t):
        count[ord(cs) - ord('a')] += 1
        count[ord(ct) - ord('a')] -= 1

    return all(x == 0 for x in count)

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("aacc", "ccac"))        # False

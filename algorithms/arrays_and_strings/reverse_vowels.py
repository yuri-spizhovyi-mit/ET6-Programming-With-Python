def reverse_vowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        # Move left forward if not vowel
        while left < right and s[left] not in vowels:
            left += 1
        # Move right backward if not vowel
        while left < right and s[right] not in vowels:
            right -= 1
        # Swap vowels
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


print(reverse_vowels("leetcode"))  # "leotcede"
print(reverse_vowels("hello"))  # "holle"
print(reverse_vowels("aA"))  # "Aa"

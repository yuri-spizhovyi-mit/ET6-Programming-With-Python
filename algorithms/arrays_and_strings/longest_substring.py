def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window until s[right] is not in the set
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("abcabcbb"))

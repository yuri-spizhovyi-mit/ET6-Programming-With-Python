def longest_common_prefix(strs: list[str]) -> str:
    # Handle edge case: empty input list
    if not strs:
        return ""

    # Start with the first word as the initial prefix
    prefix = strs[0]

    # Compare prefix with each remaining word
    for word in strs[1:]:
        # Shrink prefix until it matches the start of the current word
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # Remove last character from prefix
            if not prefix:
                return ""  # No common prefix exists

    return prefix  # Final common prefix after all comparisons



def test_longest_common_prefix():
    test_cases = [
        ([""], ""),
        (["a"], "a"),
        (["ab", "a"], "a"),
        (["abc", "def"], ""),
        (["abc", "abc", "abc"], "abc"),
        (["abc", "abcd", "abcde"], "abc"),
        (["prefix", "", "pre"], ""),
        ([], ""),
        (["longestprefix"], "longestprefix")
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = longest_common_prefix(input_data)
        assert result == expected, f"Test {i + 1} failed: got '{result}', expected '{expected}'"
    print("✅ All edge cases passed.")


# Run the test
test_longest_common_prefix()

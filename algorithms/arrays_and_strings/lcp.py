def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


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

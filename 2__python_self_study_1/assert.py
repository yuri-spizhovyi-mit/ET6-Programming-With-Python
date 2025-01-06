def validate_strings(strings):
    assert len(strings) > 0, "The list of strings cannot be empty"
    for s in strings:
        assert len(s) >= 3, f"String '{s}' is too short"
    return True

print(validate_strings(["abc", "hello", "world"]))  # True
#print(validate_strings(["ab", "world"]))           # Raises AssertionError

def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for c, w in zip(pattern, words):
        print(c, "→", w)
        if (c in char_to_word and char_to_word[c] != w) or (
            w in word_to_char and word_to_char[w] != c
        ):
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    print(char_to_word)
    print(word_to_char)
    return True


# print(word_pattern("abba", "dog cat cat dog"))  # True
# print(word_pattern("abba", "dog cat cat fish")) # False
# print(word_pattern("aaaa", "dog cat cat dog"))  # False
# print(word_pattern("abba", "dog dog dog dog"))  # False
print(word_pattern("abcabc", "dog cat rat dog cat rat"))  # True

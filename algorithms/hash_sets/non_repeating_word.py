import re


def first_unique_word(sentence: str) -> str:
    words = re.findall(r"\b[a-z]+\b", sentence.lower())  # Extract words only
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    for word in words:
        if freq[word] == 1:
            return word

    return None


print(first_unique_word("Apple banana apple orange banana kiwi"))  # "orange"
print(first_unique_word("Hi hi Hello hello"))  # None
print(first_unique_word("Dog, cat! fish... dog cat."))  # "fish"

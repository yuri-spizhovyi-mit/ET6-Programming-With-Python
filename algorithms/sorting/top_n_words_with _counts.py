from collections import Counter


def top_n_words_with_counts(words, n):
    freq = Counter(words)
    # Sort by frequency (descending), then reverse alphabetical order if tied
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    return sorted_items[:n]


words = [
    "apple",
    "banana",
    "apple",
    "cherry",
    "banana",
    "banana",
    "apple",
    "date",
    "date",
    "date",
]
print(top_n_words_with_counts(words, 3))

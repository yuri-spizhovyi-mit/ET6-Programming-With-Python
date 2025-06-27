from collections import Counter


def top_n_words(words, n):
    freq = Counter(words)
    # Step 1: sort by frequency desc, then word desc (reverse alpha)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    # Step 2: reverse alphabetical order for tie-breaker
    sorted_items = sorted(sorted_items, key=lambda x: (-x[1], x[0]))
    # Step 3: extract only words, limit to top n
    return [word for word, count in sorted_items[:n]]

words = ["apple", "banana", "apple", "cherry", "banana", "banana", "apple", "date", "date", "date"]
print(top_n_words(words, 3))

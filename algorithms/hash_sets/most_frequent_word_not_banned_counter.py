import re
from collections import Counter


def most_frequent_word_not_banned(sentence: str, banned: list[str]) -> str:
    words = re.findall(r"\b[a-z]+\b", sentence.lower())  # Extract words only

    # count all words
    freq = Counter(words)

    for word in banned:
        freq.pop(word, None)

    return freq.most_common(1)[0][0] if freq else None


sentence = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_frequent_word_not_banned(sentence, banned))
# Output: "ball"

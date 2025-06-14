import re


def most_frequent_word_not_banned(sentence: str, banned: list[str]) -> str:
    words = re.findall(r"\b[a-z]+\b", sentence.lower())  # Extract words only
    freq = {}

    for word in words:
        if word not in banned:
            freq[word] = freq.get(word, 0) + 1

    return max(freq, key=freq.get) if freq else None


sentence = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_frequent_word_not_banned(sentence, banned))
# Output: "ball"

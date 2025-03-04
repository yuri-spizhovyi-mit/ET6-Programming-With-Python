def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function

    return word in wordList and all(
        hand.get(char, 0) >= word.count(char) for char in word
    )


# print(isValidWord('word', {'w': 1, 'o': 1, 'r': 1, 'd': 1 }, ['word', 'abc']))
print(isValidWord("wordd", {"w": 1, "o": 1, "r": 1, "d": 2}, ["wordd", "abc"]))

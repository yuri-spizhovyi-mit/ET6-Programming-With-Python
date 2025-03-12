
word = "quail"
hand = {'a': 1, 'u': 1, 'l': 1, 'q': 2, 'i': 1, 'k': 1}


def update(word):
    for letter in word:
        if letter in hand and hand[letter] > 0:
            hand[letter] -= 1
            if hand[letter] == 0:
                del hand[letter]
        else:
            return False
    print(hand)
    return True


print(update(word))

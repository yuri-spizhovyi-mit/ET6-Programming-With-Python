# monkey_madlib.py

import random
import string
from word_loader import load_word_categories

# Load categorized words from the other file
nouns, verbs, adjectives, adverbs = load_word_categories()


def generate_random_string(length=10):
    return "".join(random.choices(string.ascii_uppercase, k=length))


def find_valid_words(s):
    results = {"noun": [], "verb": [], "adj": [], "adv": []}
    s = s.lower()
    for i in range(len(s)):
        for l in [5, 4, 3]:
            if l == 3 and random.random() > 0.1:
                continue
            if i + l <= len(s):
                word = s[i : i + l]
                if word in nouns:
                    results["noun"].append(word.upper())
                elif word in verbs:
                    results["verb"].append(word.upper())
                elif word in adjectives:
                    results["adj"].append(word.upper())
                elif word in adverbs:
                    results["adv"].append(word.upper())
    return results


def monkey_mad_lib():
    while True:
        rstr = generate_random_string()
        words = find_valid_words(rstr)

        if all(len(words[key]) >= 1 for key in ["noun", "verb", "adj"]):
            print(f"\nRandom String: {rstr}")
            print(
                f"I can {words['verb'][0]} but I can't {words['verb'][1] if len(words['verb']) > 1 else words['verb'][0]}."
            )
            print(f"My {words['noun'][0]} is {words['adj'][0]}.")
            break


if __name__ == "__main__":
    monkey_mad_lib()

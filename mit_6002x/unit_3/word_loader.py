# word_loader.py

import nltk
from nltk.corpus import wordnet as wn

# Make sure required resources are available
nltk.download("wordnet")
nltk.download("omw-1.4")


def get_words_by_pos(pos_tag, min_len=3, max_len=5):
    words = set()
    for synset in wn.all_synsets(pos_tag):
        for lemma in synset.lemmas():
            name = lemma.name().replace("_", "").lower()
            if name.isalpha() and min_len <= len(name) <= max_len:
                words.add(name)
    return words


def load_word_categories():
    nouns = get_words_by_pos("n")
    verbs = get_words_by_pos("v")
    adjectives = get_words_by_pos("a")
    adverbs = get_words_by_pos("r")
    return nouns, verbs, adjectives, adverbs

import re

WORDLIST_FILENAME = (
    r"C:\Users\yspizhoviy\ET6-Programming-With-Python\mit_6001x\unit_2\words.txt"
)
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

# WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE...
    flag = True
    for char in secretWord:
        if char not in lettersGuessed:
            flag = False
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    # FILL IN YOUR CODE HERE...
    temp_guessed = []
    for char in secretWord:
        if char not in lettersGuessed:
            temp_guessed.append("_")
        else:
            temp_guessed.append(char)
    return " ".join(temp_guessed)


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE...
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    for char in lettersGuessed:
        available_letters = available_letters.replace(char, "")
    return available_letters


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE...

    guesses = 8
    lettersGuessed = []
    guessed_word = ""
    print(
        f"Welcome to the game Hangman!\nI am thinking of a word that is {len(secretWord)} letters long."
    )
    print("-------------")
    while (guesses > 0) and (guessed_word != secretWord):
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
        letter = input("Please guess a letter: ")
        if letter in lettersGuessed:
            print(
                f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}"
            )
        elif letter in secretWord:
            lettersGuessed.append(letter)
            guessed_word = getGuessedWord(secretWord, lettersGuessed).replace(" ", "")
            print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
        else:
            print(
                f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}"
            )
            guesses -= 1
            lettersGuessed.append(letter)
        print("-------------")
    if guessed_word == secretWord:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "y"
hangman(secretWord)

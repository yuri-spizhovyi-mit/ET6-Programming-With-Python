"""
A program that guesses a secret number!

Created on 2024-12-06
Author: @Yurii Spizhovyi
"""

print("Please think of a number between 0 and 100! ")

low = 0
high = 100
mid = (high + low) // 2
ans = ""
run = True
while run:
    ans = input(
        "Is your secret number "
        + str(mid)
        + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
    )

    if ans == "h":
        high = mid
        mid = (high + low) // 2
    elif ans == "l":
        low = mid
        mid = (high + low) // 2
    elif ans == "c":
        print("Game over. Your secret number was: " + str(mid))
        run = False
    else:
        print("Sorry, I did not understand your input.")

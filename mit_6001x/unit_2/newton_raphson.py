epsilon = 0.01
y = 25.0
guess = y / 2.0
num_guess = 0

while abs(guess * guess - y) >= epsilon:
    num_guess += 1
    guess = guess - (((guess**2) - y) / (2 * guess))
print("num_guesses = " + str(num_guess))
print("square root of " + str(y) + " is about " + str(guess))

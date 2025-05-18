import random


def draw_simulation():
    basket = ["R", "R", "R", "G", "G", "G"]
    random.shuffle(basket)
    return basket[:3]


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """
    # Your code here
    same_color_num = 0
    for _ in range(numTrials):
        draw = draw_simulation()
        if draw.count("R") == 3 or draw.count("G") == 3:
            same_color_num += 1
    return same_color_num / numTrials


print(noReplacementSimulation(10000))

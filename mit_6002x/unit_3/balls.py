import random


def draw_simulation():
    basket = ["R", "R", "R", "G", "G", "G"]
    random.shuffle(basket)
    return basket[:3]


def noReplacementSimulation(num_trials):
    same_color_num = 0
    for _ in range(num_trials):
        draw = draw_simulation()
        if draw.count("R") == 3 or draw.count("G") == 3:
            same_color_num += 1
    same_color_probability = same_color_num / num_trials
    return same_color_probability


print(noReplacementSimulation(100000))

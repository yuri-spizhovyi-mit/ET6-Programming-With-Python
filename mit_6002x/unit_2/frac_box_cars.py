import random


def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def frac_box_cars(num_tests):
    num_box_cars = 0
    for i in range(num_tests):
        if roll_die() == 6 and roll_die() == 6:
            num_box_cars += 1
    return num_box_cars / num_tests


print(f"Frequency of double 6 = {frac_box_cars(1000000) * 100.0:2f}%")

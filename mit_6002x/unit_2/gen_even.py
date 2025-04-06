import random


def gen_even():
    return random.choice(range(0, 100, 2))


print(gen_even())

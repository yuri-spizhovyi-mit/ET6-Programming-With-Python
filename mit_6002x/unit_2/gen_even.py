import random


def gen_even():
    return random.choice(range(10, 21, 2))


print(gen_even())

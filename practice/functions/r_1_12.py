import random


def random_choice(l: list):
    if not l:
        raise ValueError("List can not be empty")
    i = random.randrange(0, len(l))
    return l[i]


print(random_choice(["A", "B", "C", "D"]))

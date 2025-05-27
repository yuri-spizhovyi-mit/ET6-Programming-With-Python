import random


def shuffle(l: list):
    shuffled = []
    while l:
        random_index = random.randint(0, len(l) - 1)
        shuffled.append(l.pop(random_index))
    return shuffled


print(shuffle([1, 2, 3, 4, 5]))


def shuffle2(l: list):
    for i in range(len(l) - 1, 0, -1):
        j = random.randint(0, i)
        l[i], l[j] = l[j], l[i]
    return l


print(shuffle2([1, 2, 3, 4, 5]))

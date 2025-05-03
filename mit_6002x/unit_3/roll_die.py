import random


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def run(trials):
    results = {}
    for _ in range(trials):
        output = roll_die()
        results[output] = results.get(output, 0) + 1

    return results


print(run(1000))

import random


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def pascal_simulation(num_trials):
    """Assumes num_trials an int > 0
    Prints an estimate of the probability of winning"""
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print("Probability of winning = ", num_wins / num_trials)


pascal_simulation(1000)

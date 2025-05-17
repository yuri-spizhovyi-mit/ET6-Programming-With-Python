import random


def flip(num_flips):
    """Assumes num_flips a positive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(["T", "H"]) == "H":
            heads += 1
    return heads / num_flips


def flip_simulation(num_flips_per_trial, num_trials):
    """Assume num_flips and num_trials positive int"""
    frac_head = []
    for i in range(num_trials):
        frac_head.append(flip(num_flips_per_trial))
    mean = sum(frac_head) / len(frac_head)
    return mean


print(flip_simulation(10, 50))

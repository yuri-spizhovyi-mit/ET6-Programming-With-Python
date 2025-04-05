import random


def flip(numFlips):
    """Assumes numFlips a positive int"""
    heads = 0
    for i in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / numFlips


def flipSim(numFlipsPerTrial, numTrials):
    """Assumes numFlipsPerTrial and numTrials positive ints"""
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
        mean = sum(fracHeads) / len(fracHeads)
    return mean


for i in range(10):
    print(flipSim(10, 100))

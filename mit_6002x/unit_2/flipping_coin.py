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


# print('Mean = ', flipSim(100, 20000))
mean = flipSim(100, 100000)
print(f"Mean = {mean:.4f}")
print(f"Mean = {mean:.10g}")
# print(flip(10))

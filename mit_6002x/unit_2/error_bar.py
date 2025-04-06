import random
import pylab
import numpy as np


def flip(numFlips):
    """Simulate flipping a coin numFlips times, return fraction of heads."""
    heads = 0
    for _ in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / numFlips


def variance(X):
    mean = sum(X) / len(X)
    return sum((x - mean) ** 2 for x in X) / len(X)


def stdDev(X):
    return variance(X) ** 0.5


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = [flip(numFlipsPerTrial) for _ in range(numTrials)]
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return fracHeads, mean, sd


def showErrorBars(minExp, maxExp, numTrials):
    """Plot mean fraction of heads with 95% confidence interval error bars."""
    means, sds, xVals = [], [], []

    for exp in range(minExp, maxExp + 1):
        flips = 2**exp
        xVals.append(flips)
        _, mean, sd = flipSim(flips, numTrials)
        means.append(mean)
        sds.append(sd)

    yErr = 1.96 * np.array(sds)  # 95% confidence interval
    pylab.errorbar(xVals, means, yerr=yErr, fmt="o")
    pylab.semilogx()
    pylab.title(f"Mean Fraction of Heads ({numTrials} trials)")
    pylab.xlabel("Number of flips per trial")
    pylab.ylabel("Fraction of heads ± 95% confidence")
    pylab.grid(True)
    pylab.show()


def main():
    showErrorBars(minExp=4, maxExp=10, numTrials=100)


if __name__ == "__main__":
    main()

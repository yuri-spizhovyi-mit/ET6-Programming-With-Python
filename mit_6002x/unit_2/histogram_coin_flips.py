import random
import pylab


def flip(numFlips):
    """Simulate flipping a fair coin numFlips times. Return fraction of heads."""
    heads = 0
    for _ in range(numFlips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / float(numFlips)


def variance(X):
    mean = sum(X) / len(X)
    return sum((x - mean) ** 2 for x in X) / len(X)


def stdDev(X):
    return variance(X) ** 0.5


def flipSim(numFlipsPerTrial, numTrials):
    """Run multiple trials of numFlipsPerTrial flips each. Return results, mean, and SD."""
    fracHeads = []
    for _ in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return fracHeads, mean, sd


def labelPlot(numFlips, numTrials, mean, sd):
    """Add title, labels, and annotations to the plot."""
    pylab.title(f"{numTrials} trials of {numFlips} flips each")
    pylab.xlabel("Fraction of Heads")
    pylab.ylabel("Number of Trials")
    pylab.annotate(
        f"Mean = {round(mean, 4)}\nSD = {round(sd, 4)}",
        size="x-large",
        xy=(0.67, 0.5),
        xycoords="axes fraction",
    )


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)

    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)

    pylab.show()


def main():
    makePlots(100, 1000, 100000)


if __name__ == "__main__":
    main()

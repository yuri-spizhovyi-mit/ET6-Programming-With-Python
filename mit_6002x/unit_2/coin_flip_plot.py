import random
import pylab  # part of matplotlib


def makePlot(xVals, yVals, title, xLabel, yLabel, style, logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


def runTrial(numFlips):
    numHeads = 0
    for _ in range(numFlips):
        if random.choice(("H", "T")) == "H":
            numHeads += 1
    numTails = numFlips - numHeads
    return numHeads, numTails


def variance(X):
    mean = sum(X) / len(X)
    return sum((x - mean) ** 2 for x in X) / len(X)


def stdDev(X):
    return variance(X) ** 0.5


def flipPlot1(minExp, maxExp, numTrials):
    """Assumes minExp, maxExp, numTrials are ints > 0; minExp < maxExp.
    Plots summaries of results of numTrials trials of 2**minExp to 2**maxExp coin flips."""
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = [2**exp for exp in range(minExp, maxExp + 1)]

    for numFlips in xAxis:
        ratios, diffs = [], []
        for _ in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            if numTails == 0:  # avoid division by zero
                ratio = float("inf")
            else:
                ratio = numHeads / numTails
            ratios.append(ratio)
            diffs.append(abs(numHeads - numTails))

        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))

    numTrialsString = f" ({numTrials} Trials)"

    makePlot(
        xAxis,
        ratiosMeans,
        "Mean Heads/Tails Ratios" + numTrialsString,
        "Number of Flips",
        "Mean Heads/Tails",
        "ko",
        logX=True,
    )
    makePlot(
        xAxis,
        ratiosSDs,
        "SD Heads/Tails Ratios" + numTrialsString,
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )
    pylab.show()


# 👇 Add this to allow the script to run only when it's executed directly
def main():
    minExp = 4
    maxExp = 20
    numTrials = 20
    flipPlot1(minExp, maxExp, numTrials)


if __name__ == "__main__":
    main()

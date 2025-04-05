import random
import pylab


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


def CV(X):
    mean = sum(X) / len(X)
    if mean == 0:
        return float("nan")  # Avoid division by zero
    return stdDev(X) / mean


def flipPlot2(minExp, maxExp, numTrials):
    """Plots mean, SD, and Coefficient of Variation (CV) for ratios and differences"""
    ratiosMeans, diffsMeans = [], []
    ratiosSDs, diffsSDs = [], []
    ratiosCVs, diffsCVs = [], []
    xAxis = [2**exp for exp in range(minExp, maxExp + 1)]

    for numFlips in xAxis:
        ratios, diffs = [], []
        for _ in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratio = numHeads / float(numTails) if numTails != 0 else float("inf")
            ratios.append(ratio)
            diffs.append(abs(numHeads - numTails))

        # Calculate means, std devs, and CVs
        ratiosMeans.append(sum(ratios) / numTrials)
        diffsMeans.append(sum(diffs) / numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))

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
    makePlot(
        xAxis,
        diffsMeans,
        "Mean abs(#Heads - #Tails)" + numTrialsString,
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "ko",
        logX=True,
        logY=True,
    )
    makePlot(
        xAxis,
        diffsSDs,
        "SD abs(#Heads - #Tails)" + numTrialsString,
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )
    makePlot(
        xAxis,
        diffsCVs,
        "Coeff. of Var. abs(#Heads - #Tails)" + numTrialsString,
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
    )
    makePlot(
        xAxis,
        ratiosCVs,
        "Coeff. of Var. Heads/Tails Ratio" + numTrialsString,
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
        logY=True,
    )

    pylab.show()  # Show all plots at once


def main():
    minExp = 4
    maxExp = 10
    numTrials = 100
    flipPlot2(minExp, maxExp, numTrials)


if __name__ == "__main__":
    main()

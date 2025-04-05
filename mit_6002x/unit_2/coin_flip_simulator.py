import random
import pylab
import math

def stdDev(X):
    """Return standard deviation of a list of numbers."""
    mean = sum(X) / len(X)
    total = sum((x - mean) ** 2 for x in X)
    return math.sqrt(total / len(X))

def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX=False, logY=False):
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
    for n in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    """Assumes minExp, maxExp, numTrials ints >0; minExp < maxExp.
    Plots summaries of results of numTrials trials of
    2**minExp to 2**maxExp coin flips."""
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            if numTails == 0:
                continue  # Avoid divide-by-zero
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        
        ratiosMeans.append(sum(ratios) / len(ratios))
        diffsMeans.append(sum(diffs) / len(diffs))
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))

    numTrialsString = f' ({numTrials} Trials)'

    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of Flips',
             'Mean Heads/Tails', 'ko', logX=True)

    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips',
             'Standard Deviation', 'ko', logX=True, logY=True)

# Example call
random.seed(0)
flipPlot1(4, 10, 100)
pylab.show()

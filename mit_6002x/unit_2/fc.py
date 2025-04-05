import random
import pylab

def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp.
    Plots results of 2**minExp to 2**maxExp coin flips."""
    ratios, diffs, xAxis = [], [], []
    
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue

    pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'k')

    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')

# Set a fixed seed for reproducibility
random.seed(0)
flipPlot(4, 20)
pylab.show()

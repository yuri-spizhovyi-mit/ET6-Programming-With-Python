import random
import pylab  # or use matplotlib.pyplot as plt


# Simulate one 7-game series
def playSeries(numGames, teamProb):
    numWon = 0
    for game in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return numWon > numGames // 2  # Returns True if team wins majority of games


# Run many series simulations and return the fraction won
def fractionWon(teamProb, numSeries, seriesLen):
    won = 0
    for series in range(numSeries):
        if playSeries(seriesLen, teamProb):
            won += 1
    return won / float(numSeries)


# Run full simulation across a range of team strengths
def simSeries(numSeries):
    prob = 0.5
    fracsWon, probs = [], []

    while prob <= 1.0:
        fracsWon.append(fractionWon(prob, numSeries, 7))
        probs.append(prob)
        prob += 0.01

    pylab.axhline(0.95, color="gray", linestyle="--")  # Reference line at 95%
    pylab.plot(probs, fracsWon, "k", linewidth=2)
    pylab.xlabel("Probability of Winning a Game")
    pylab.ylabel("Probability of Winning a Series")
    pylab.title(str(numSeries) + " Simulated Seven-Game Series")
    pylab.grid(True)
    pylab.show()


# Run simulation with 400 series per point
simSeries(400)

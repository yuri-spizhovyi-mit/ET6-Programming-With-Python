import random
import matplotlib.pyplot as plt


# Simulate one series
def playSeries(numGames, teamProb):
    numWon = 0
    for _ in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return numWon > numGames // 2


# Run many series and calculate win fraction
def fractionWon(teamProb, numSeries, seriesLen):
    won = 0
    for _ in range(numSeries):
        if playSeries(seriesLen, teamProb):
            won += 1
    return won / numSeries


# User inputs
teamProb = float(input("Enter your team's probability of winning a game (e.g. 0.6): "))
numSeries = int(input("Enter number of series to simulate (e.g. 1000): "))
seriesLen = 7  # Best-of-7 series

# Run simulation
seriesWinRate = fractionWon(teamProb, numSeries, seriesLen)
print(
    f"With a game win chance of {teamProb:.2f}, your team won the series {seriesWinRate * 100:.1f}% of the time."
)

# Show on chart
plt.bar(
    ["Game Win %", "Series Win %"],
    [teamProb * 100, seriesWinRate * 100],
    color=["blue", "green"],
)
plt.ylim(0, 100)
plt.ylabel("Winning Percentage")
plt.title("Game vs Series Winning Chances")
plt.grid(True, axis="y", linestyle="--", linewidth=0.5)
plt.show()

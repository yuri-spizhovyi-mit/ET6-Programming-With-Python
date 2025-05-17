import pylab
import random


def flip(num_flips):
    """Simulate flipping a fair coin numFlips times and return the fraction of heads."""
    heads = 0
    for _ in range(num_flips):
        if random.random() < 0.5:
            heads += 1
    return heads / num_flips


def regressToMean(num_flips, num_trials):
    """Demonstrate regression to the mean with simulated coin flips."""
    # Get fraction of heads for each trial
    frac_heads = [flip(num_flips) for _ in range(num_trials)]

    # Find trials with extreme results and the following trial
    extremes = []
    next_trials = []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i + 1])

    # Plot results
    pylab.figure(figsize=(10, 5))
    pylab.plot(range(len(extremes)), extremes, "ro", label="Extreme")
    pylab.plot(range(len(next_trials)), next_trials, "k^", label="Next Trial")
    pylab.axhline(0.5, color="gray", linestyle="--")
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel("Extreme Example Index")
    pylab.ylabel("Fraction Heads")
    pylab.title("Regression to the Mean")
    pylab.legend(loc="best")
    pylab.show()


# Run the simulation
regressToMean(15, 40)

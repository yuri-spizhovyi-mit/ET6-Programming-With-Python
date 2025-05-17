import random
import math
import matplotlib.pyplot as plt


def run_trial(num_flips):
    """Simulates flipping a fair coin num_flips times."""
    heads = sum(1 for _ in range(num_flips) if random.random() < 0.5)
    tails = num_flips - heads
    return heads, tails


def std_dev(data):
    """Calculates the sample standard deviation of a list of numbers."""
    if len(data) < 2:
        return 0
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)


def cv(data):
    """Calculates the coefficient of variation of a list of numbers."""
    mean = sum(data) / len(data)
    return std_dev(data) / mean if mean != 0 else 0


def make_plot(x, y, title, xlabel, ylabel, style, logX=False, logY=False):
    """Creates a plot using matplotlib."""
    plt.figure()
    plt.plot(x, y, style)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if logX:
        plt.xscale("log")
    if logY:
        plt.yscale("log")
    plt.grid(True)
    plt.show()


def flip_plot2(min_exp, max_exp, num_trials):
    """
    Plots results of num_trials coin flip experiments,
    ranging from 2**min_exp to 2**max_exp flips.
    Includes mean, SD, and coefficient of variation for heads/tails ratio and absolute difference.
    """
    x_axis = []
    ratios_means, diffs_means = [], []
    ratios_sds, diffs_sds = [], []
    ratios_cvs, diffs_cvs = [], []

    for exp in range(min_exp, max_exp + 1):
        num_flips = 2**exp
        x_axis.append(num_flips)

        ratios = []
        diffs = []

        for _ in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratio = num_heads / num_tails if num_tails != 0 else 0
            ratios.append(ratio)
            diffs.append(abs(num_heads - num_tails))

        # Aggregate statistics
        ratios_means.append(sum(ratios) / num_trials)
        diffs_means.append(sum(diffs) / num_trials)
        ratios_sds.append(std_dev(ratios))
        diffs_sds.append(std_dev(diffs))
        ratios_cvs.append(cv(ratios))
        diffs_cvs.append(cv(diffs))

    trial_label = f" ({num_trials} Trials)"

    make_plot(
        x_axis,
        ratios_means,
        f"Mean Heads/Tails Ratios{trial_label}",
        "Number of Flips",
        "Mean Heads/Tails",
        "ko",
        logX=True,
    )

    make_plot(
        x_axis,
        ratios_sds,
        f"SD Heads/Tails Ratios{trial_label}",
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )

    make_plot(
        x_axis,
        diffs_means,
        f"Mean abs(#Heads - #Tails){trial_label}",
        "Number of Flips",
        "Mean abs(#Heads - #Tails)",
        "ko",
        logX=True,
        logY=True,
    )

    make_plot(
        x_axis,
        diffs_sds,
        f"SD abs(#Heads - #Tails){trial_label}",
        "Number of Flips",
        "Standard Deviation",
        "ko",
        logX=True,
        logY=True,
    )

    make_plot(
        x_axis,
        diffs_cvs,
        f"Coeff. of Var. abs(#Heads - #Tails){trial_label}",
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
    )

    make_plot(
        x_axis,
        ratios_cvs,
        f"Coeff. of Var. Heads/Tails Ratio{trial_label}",
        "Number of Flips",
        "Coeff. of Var.",
        "ko",
        logX=True,
        logY=True,
    )


# Example call
flip_plot2(min_exp=4, max_exp=10, num_trials=100)

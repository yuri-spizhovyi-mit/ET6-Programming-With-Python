import numpy as np


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """

    error = sum([(y[i] - estimated[i]) ** 2 for i in range(len(y))])
    mean_error = error / len(y)
    return 1 - (mean_error / np.var(y))


print(r_squared([32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0]))

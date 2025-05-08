import pylab
import numpy as np


def getData(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()[1:]  # Skip header
    x, y = [], []
    for line in lines:
        xi, yi = line.strip().split()
        x.append(float(yi))
        y.append(float(xi))
    return np.array(x), np.array(y)


def rSquare(measured, estimated):
    SEE = ((estimated - measured) ** 2).sum()
    mMean = measured.mean()
    MV = ((mMean - measured) ** 2).sum()
    return 1 - SEE / MV


def plotFits(x, y):
    pylab.plot(x, y, "bo", label="Data")
    degrees = [2, 4, 8, 16]
    colors = ["green", "red", "cyan", "magenta"]
    for deg, color in zip(degrees, colors):
        coeffs = pylab.polyfit(x, y, deg)
        estY = pylab.polyval(coeffs, x)
        r2 = rSquare(y, estY)
        pylab.plot(
            x,
            estY,
            color=color,
            linewidth=2,
            label=f"Fit of degree {deg}, R2 = {round(r2, 5)}",
        )
    pylab.title("Mystery Data")
    pylab.legend(loc="best")
    pylab.show()


x, y = getData("mysteryData.txt")
plotFits(x, y)

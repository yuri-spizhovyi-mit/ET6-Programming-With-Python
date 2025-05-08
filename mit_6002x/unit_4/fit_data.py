import pylab, random


def getData(fileName):
    dataFile = open(fileName, "r")
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)


def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
    estimate: one dimensional array of predicted values"""
    SEE = ((estimated - measured) ** 2).sum()
    mMean = measured.sum() / float(len(measured))
    MV = ((mMean - measured) ** 2).sum()
    return 1 - SEE / MV


def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals * 9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, "bo", label="Measured points")
    pylab.title("Measured Displacement of Spring")
    pylab.xlabel("Force (Newtons)")
    pylab.ylabel("Distance (meters)")

    a, b = pylab.polyfit(xVals, yVals, 1)  # fit y = ax + b
    estYVals = a * xVals + b
    k = 1 / a
    r2 = rSquare(yVals, estYVals)  # Compute R²

    pylab.plot(
        xVals, estYVals, label=f"Linear fit, k = {round(k, 5)}, R² = {round(r2, 4)}"
    )
    pylab.legend(loc="best")


fitData("springData.txt")
pylab.show()

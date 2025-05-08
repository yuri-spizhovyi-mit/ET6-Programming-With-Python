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


def fitData3(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals[:-6])
    yVals = pylab.array(yVals[:-6])
    xVals = xVals * 9.81  # convert mass to force (F = mg)
    pylab.plot(xVals, yVals, "bo", label="Measured points")
    pylab.title("Measured Displacement of Spring (Elastic Region Only)")
    pylab.xlabel("Force (Newtons)")
    pylab.ylabel("Distance (meters)")

    a, b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a * xVals + b
    k = 1 / a
    r2 = rSquare(yVals, estYVals)  # Compute R²

    pylab.plot(
        xVals, estYVals, label=f"Linear fit, k = {round(k, 5)}, R² = {round(r2, 4)}"
    )
    pylab.legend(loc="best")


def compareFits(fileName):
    import matplotlib.pyplot as plt

    # ---- Fit Full Dataset ----
    xVals_full, yVals_full = getData(fileName)
    x_full = pylab.array(xVals_full) * 9.81
    y_full = pylab.array(yVals_full)
    a1, b1 = pylab.polyfit(x_full, y_full, 1)
    estY_full = a1 * x_full + b1
    r2_full = rSquare(y_full, estY_full)

    # ---- Fit Elastic Region Only ----
    xVals_elastic = xVals_full[:-6]
    yVals_elastic = yVals_full[:-6]
    x_elastic = pylab.array(xVals_elastic) * 9.81
    y_elastic = pylab.array(yVals_elastic)
    a2, b2 = pylab.polyfit(x_elastic, y_elastic, 1)
    estY_elastic = a2 * x_elastic + b2
    r2_elastic = rSquare(y_elastic, estY_elastic)

    # ---- Plot ----
    pylab.figure("Full Data")
    fitData(fileName)
    pylab.figure("Elastic Only")
    fitData3(fileName)
    pylab.show()

    # ---- Print Comparison ----
    print(f"R² (Full Data):    {round(r2_full, 4)}")
    print(f"R² (Elastic Only): {round(r2_elastic, 4)}")
    if r2_elastic > r2_full:
        print("✅ Removing nonlinear data improved the fit (higher R²).")
    else:
        print("⚠️  Removing data did not improve the fit.")


compareFits("springData.txt")

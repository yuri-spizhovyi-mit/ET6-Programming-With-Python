import pylab


def plot_housing(impression):
    """
    Plots a bar chart of housing prices over time for the U.S. Midwest.

    Parameters:
    - impression: str, must be one of 'flat', 'volatile', or 'fair'

    Raises:
    - ValueError: if impression is not one of the accepted values
    """
    with open("midWestHousingPrices.txt", "r") as f:
        labels, prices = [], []
        for line in f:
            year, quarter, price = line.split()
            label = year[2:4] + "\nQ" + quarter[1]
            labels.append(label)
            prices.append(int(price) / 1000)

    quarters = pylab.arange(len(labels))  # x coordinates of bars
    width = 0.8  # width of bars

    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters + width / 2, labels)
    pylab.title("Housing Prices in U.S. Midwest")
    pylab.xlabel("Quarter")
    pylab.ylabel("Average Price ($1,000's)")

    if impression == "flat":
        pylab.ylim(1, 500)
    elif impression == "volatile":
        pylab.ylim(180, 220)
    elif impression == "fair":
        pylab.ylim(150, 250)
    else:
        raise ValueError("Impression must be one of: 'flat', 'volatile', or 'fair'")


# Example usage
plot_housing("flat")
pylab.figure()
plot_housing("volatile")
pylab.show()

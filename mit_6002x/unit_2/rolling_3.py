import pylab
# from math import factorial


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def rolling_3(n):
    if n < 2:
        return 0

    bin_coef = factorial(n) / (factorial(2) * factorial(n - 2))
    probability = bin_coef * (1 / 6) ** 2 * (5 / 6) ** (n - 2)
    return probability


data = []
x_values = range(2, 101)
for i in x_values:
    data.append(rolling_3(i))

pylab.plot(x_values, data, label="Probability of rolling two 3's")
pylab.xlabel("Number of trials")
pylab.ylabel("Probability of two 3's")
pylab.title("Probability of rolling two 3's")
pylab.legend()
pylab.show()
# print(data)

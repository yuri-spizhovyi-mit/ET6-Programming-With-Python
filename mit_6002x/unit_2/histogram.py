import pylab
import random

vals = []
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins=10)
pylab.ylabel("Number of Occurences")
pylab.xlabel("Sum of Two Random Integers (0–100)")
pylab.title("Histogram of Sums from Two Random Integers")
pylab.show()

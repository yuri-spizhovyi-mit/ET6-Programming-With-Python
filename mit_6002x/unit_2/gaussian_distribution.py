import random
import math
from scipy.integrate import quad

def gaussian(x, mu, sigma):
    """Standard Gaussian (normal) distribution function."""
    factor1 = 1.0 / (sigma * math.sqrt(2 * math.pi))
    factor2 = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2

def checkEmpirical(numTrials):
    """Run multiple trials to check the empirical rule numerically."""
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print(f"\nTrial {t+1}: mu = {mu}, sigma = {sigma}")
        for numStd in (1, 2, 3):
            # Integrate the Gaussian curve within ±1σ, ±2σ, ±3σ of the mean
            area, _ = quad(lambda x: gaussian(x, mu, sigma),
                           mu - numStd * sigma, mu + numStd * sigma)
            print(f"  Fraction within {numStd} std = {round(area, 4)}")

def main():
    checkEmpirical(3)

if __name__ == "__main__":
    main()

import random
import math
from scipy.integrate import quad


class GaussianEmpiricalCheck:
    """
    Class to evaluate the empirical rule using Gaussian distribution.
    """

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def gaussian(self, x):
        """Standard Gaussian (normal) distribution function."""
        factor1 = 1.0 / (self.sigma * math.sqrt(2 * math.pi))
        factor2 = math.exp(-((x - self.mu) ** 2) / (2 * self.sigma**2))
        return factor1 * factor2

    def compute_area(self, num_std):
        """Computes area under the Gaussian curve within ±num_std standard deviations."""
        lower = self.mu - num_std * self.sigma
        upper = self.mu + num_std * self.sigma
        area, _ = quad(self.gaussian, lower, upper)
        return round(area, 4)

    @staticmethod
    def run_trials(num_trials):
        """Run multiple trials to check the empirical rule numerically."""
        for t in range(1, num_trials + 1):
            mu = random.randint(-10, 10)
            sigma = random.randint(1, 10)
            checker = GaussianEmpiricalCheck(mu, sigma)
            print(f"\nTrial {t}: mu = {mu}, sigma = {sigma}")
            for num_std in (1, 2, 3):
                area = checker.compute_area(num_std)
                print(f"  Fraction within {num_std} std = {area}")


def main():
    GaussianEmpiricalCheck.run_trials(3)


if __name__ == "__main__":
    main()

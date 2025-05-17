import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom, expon

# Parameters
lambda_val = 4
n = 10
p = 0.4
x_discrete = np.arange(0, 15)
x_continuous = np.linspace(0, 10, 200)

# Probability mass and density functions
poisson_pmf = poisson.pmf(x_discrete, mu=lambda_val)
binomial_pmf = binom.pmf(x_discrete, n=n, p=p)
exponential_pdf = expon.pdf(x_continuous, scale=1 / lambda_val)

# Plot
plt.figure(figsize=(14, 6))

# Discrete Distributions
plt.subplot(1, 2, 1)
plt.stem(
    x_discrete,
    poisson_pmf,
    linefmt="blue",
    markerfmt="bo",
    basefmt=" ",
    label="Poisson (λ=4)",
)
plt.stem(
    x_discrete,
    binomial_pmf,
    linefmt="green",
    markerfmt="go",
    basefmt=" ",
    label="Binomial (n=10, p=0.4)",
)
plt.title("Poisson vs Binomial Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)

# Continuous Distribution
plt.subplot(1, 2, 2)
plt.plot(x_continuous, exponential_pdf, color="purple", label="Exponential (λ=4)")
plt.title("Exponential Distribution")
plt.xlabel("Time Between Events")
plt.ylabel("Density")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

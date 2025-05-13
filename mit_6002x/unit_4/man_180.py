import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 210  # mean
sigma = 30  # standard deviation

# Generate x values for the full range
x = np.linspace(120, 300, 500)
y = norm.pdf(x, mu, sigma)

# Accurate probability above 180 using Z-score
p_above_180 = 1 - norm.cdf(180, mu, sigma)

# Plot the normal distribution
plt.figure(figsize=(12, 6))
plt.plot(x, y, label="Normal Distribution", color="black")

# Fill area above 180 (weight > 180)
x_fill = np.linspace(180, 300, 500)
y_fill = norm.pdf(x_fill, mu, sigma)
plt.fill_between(
    x_fill,
    y_fill,
    color="skyblue",
    alpha=0.6,
    label=f"P(weight > 180) ≈ {p_above_180:.2%}",
)

# Draw vertical lines for mean and 1 std deviation below mean
plt.axvline(mu, color="red", linestyle="--", label="Mean (210 lbs)")
plt.axvline(mu - sigma, color="green", linestyle="--", label="180 lbs (μ - 1σ)")

# Labels and legend
plt.title("Normal Distribution of Male Weights (μ=210, σ=30)")
plt.xlabel("Weight (lbs)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Re-import libraries after environment reset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm


# 1. Estimate Pi using Monte Carlo
def estimate_pi(num_points=10000):
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    inside_circle = x**2 + y**2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    return pi_estimate, x, y, inside_circle


# 2. Simulate a basic financial return model
def simulate_portfolio_return(num_simulations=10000, mean=0.07, std_dev=0.15):
    returns = np.random.normal(mean, std_dev, num_simulations)
    final_value = 1000 * np.exp(returns)  # Initial investment of 1000
    return returns, final_value


# 3. Estimate integral of e^(-x^2) from 0 to 1
def estimate_integral(num_samples=10000):
    x = np.random.uniform(0, 1, num_samples)
    fx = np.exp(-(x**2))
    estimate = np.mean(fx) * 1
    return estimate


# Run all simulations
pi_estimate, x_pi, y_pi, inside_pi = estimate_pi()
returns, final_values = simulate_portfolio_return()
integral_estimate = estimate_integral()

# Plot Pi estimation
plt.figure(figsize=(14, 4))
plt.subplot(1, 3, 1)
plt.scatter(x_pi[inside_pi], y_pi[inside_pi], color="skyblue", s=1)
plt.scatter(x_pi[~inside_pi], y_pi[~inside_pi], color="salmon", s=1)
plt.title(f"Monte Carlo π Estimate: {pi_estimate:.4f}")
plt.axis("equal")
plt.grid(True)

# Plot financial return distribution
plt.subplot(1, 3, 2)
plt.hist(final_values, bins=30, color="lightgreen", edgecolor="black")
plt.title("Simulated Portfolio Value Distribution")
plt.xlabel("Final Value ($)")
plt.ylabel("Frequency")
plt.grid(True)

# Display integral estimate in text
plt.subplot(1, 3, 3)
plt.text(0.1, 0.5, f"Estimated ∫₀¹ e^(-x²) dx ≈ {integral_estimate:.4f}", fontsize=14)
plt.axis("off")

plt.tight_layout()
plt.show()

# Output results in table format
pd.DataFrame(
    {
        "Estimated π": [pi_estimate],
        "Estimated ∫₀¹ e^(-x²) dx": [integral_estimate],
        "Mean Final Portfolio Value": [np.mean(final_values)],
    }
)

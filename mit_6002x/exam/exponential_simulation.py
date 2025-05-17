import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set parameters
lambda_val = 3  # 3 customers per hour
num_simulations = 1000

# Simulate 1000 waiting times (in hours)
waiting_times = np.random.exponential(scale=1 / lambda_val, size=num_simulations)

# Count how many customers arrive within 20 minutes (1/3 hour)
within_20_min = np.sum(waiting_times <= 1 / 3)
probability_estimate = within_20_min / num_simulations

# Plot histogram
plt.hist(waiting_times, bins=30, color="skyblue", edgecolor="black")
plt.axvline(x=1 / 3, color="red", linestyle="--", label="20 minutes")
plt.title("Simulated Time Between Arrivals (λ = 3 per hour)")
plt.xlabel("Time Between Arrivals (hours)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Show first 10 times
df = pd.DataFrame(
    {"Wait Time (hr)": waiting_times[:10], "Wait Time (min)": waiting_times[:10] * 60}
)
print(df)

# Show estimated probability
print(
    f"\nEstimated probability of arrival within 20 minutes: {probability_estimate:.4f}"
)

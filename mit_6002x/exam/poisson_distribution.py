import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import pandas as pd
import ace_tools as tools

# Simulation parameters
lambda_val = 4  # Average number of events per interval
num_intervals = 1000  # Simulate over 1000 intervals (e.g., hours)

# Generate Poisson-distributed random data
events = np.random.poisson(lam=lambda_val, size=num_intervals)

# Create a frequency distribution
values, counts = np.unique(events, return_counts=True)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.bar(values, counts / num_intervals, width=0.8, color="skyblue", edgecolor="black")
plt.title(
    f"Simulated Poisson Distribution (λ = {lambda_val}, over {num_intervals} intervals)"
)
plt.xlabel("Number of Events per Interval")
plt.ylabel("Relative Frequency")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Prepare data for display
df = pd.DataFrame(
    {
        "Events": values,
        "Frequency": counts,
        "Relative Frequency": counts / num_intervals,
    }
)
tools.display_dataframe_to_user(name="Simulated Poisson Data", dataframe=df)

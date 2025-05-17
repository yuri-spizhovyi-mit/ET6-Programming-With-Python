import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data: heights of 100 people (e.g., in cm)
np.random.seed(0)
sample_data = np.random.normal(loc=170, scale=10, size=100)

# Calculate sample mean and standard error
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # sample standard deviation
n = len(sample_data)
standard_error = sample_std / np.sqrt(n)

# Calculate the 95% confidence interval
confidence_level = 0.95
t_score = stats.t.ppf((1 + confidence_level) / 2, df=n - 1)

margin_of_error = t_score * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(confidence_interval)

# Plot the sample data distribution and the confidence interval
plt.figure(figsize=(10, 5))
plt.hist(sample_data, bins=15, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(
    sample_mean, color="red", linestyle="--", label=f"Mean = {sample_mean:.2f} cm"
)
plt.axvline(
    confidence_interval[0],
    color="green",
    linestyle="--",
    label=f"95% CI Lower = {confidence_interval[0]:.2f} cm",
)
plt.axvline(
    confidence_interval[1],
    color="green",
    linestyle="--",
    label=f"95% CI Upper = {confidence_interval[1]:.2f} cm",
)

plt.title("Sample Heights Distribution with 95% Confidence Interval")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

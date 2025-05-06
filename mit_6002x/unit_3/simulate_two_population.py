import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# Set random seed for consistency
np.random.seed(0)

# Step 1: Simulate two populations
# Create a population with mean ~70 and low variation (SD = 5)
low_var_pop = np.random.normal(loc=70, scale=5, size=1000)

# Create a second population with the same mean but high variation (SD = 20)
high_var_pop = np.random.normal(loc=70, scale=20, size=1000)

# Step 2: Draw 10 random samples from each population
# Sample 10 values from each population using random.sample
sample_size = 10
sample_low = random.sample(list(low_var_pop), sample_size)
sample_high = random.sample(list(high_var_pop), sample_size)


# Step 3: Define a function to compute mean, SD, and CI
def summarize(sample):
    mean = np.mean(sample)
    sd = np.std(sample, ddof=1)  # ddof=1 for sample SD
    margin = 1.96 * (sd / np.sqrt(len(sample)))
    ci_lower = mean - margin
    ci_upper = mean + margin
    return mean, sd, (ci_lower, ci_upper)


# Step 4: Analyze both samples
mean_low, sd_low, ci_low = summarize(sample_low)
mean_high, sd_high, ci_high = summarize(sample_high)

# Step 5: Print results
print("Low Variation Sample:")
print("Mean:", mean_low)
print("SD:", sd_low)
print("95% Confidence Interval:", ci_low)

print("\nHigh Variation Sample:")
print("Mean:", mean_high)
print("SD:", sd_high)
print("95% Confidence Interval:", ci_high)

# Already defined: sample_low, sample_high
# Already computed: mean_low, ci_low, mean_high, ci_high

# Low variance sample
plt.figure(figsize=(10, 4))
sns.histplot(sample_low, kde=True, color="skyblue", bins=8)
plt.axvline(mean_low, color="blue", linestyle="--", label="Mean")
plt.axvline(ci_low[0], color="gray", linestyle=":", label="95% CI bounds")
plt.axvline(ci_low[1], color="gray", linestyle=":")
plt.title("Low-Variance Sample Distribution")
plt.legend()
plt.show()

# High variance sample
plt.figure(figsize=(10, 4))
sns.histplot(sample_high, kde=True, color="salmon", bins=8)
plt.axvline(mean_high, color="red", linestyle="--", label="Mean")
plt.axvline(ci_high[0], color="gray", linestyle=":", label="95% CI bounds")
plt.axvline(ci_high[1], color="gray", linestyle=":")
plt.title("High-Variance Sample Distribution")
plt.legend()
plt.show()

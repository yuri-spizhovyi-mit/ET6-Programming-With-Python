"""
Created on Wed May  7 07:32:26 2025

@author: somai
"""

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate random data following a non-normal distribution
population_data = np.random.exponential(
    scale=2, size=10000
)  # Example: Exponential distribution

# Step 2: Sampling, Calculation, and Standard Error
sample_sizes = [10, 30, 50]  # Sample sizes to test
num_samples = 1000  # Number of samples to take

for size in sample_sizes:
    sample_means = []
    # the number of times you're repeating the process of taking
    # a sample of a specific size from the population data and
    # calculating the sample mean.
    for j in range(num_samples):
        sample = np.random.choice(population_data, size=size, replace=False)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)

    # Calculate standard error
    std_err = np.std(sample_means, ddof=1) / np.sqrt(size)

    print(f"Sample Size {size}: Mean = {np.mean(sample_means)}, SE = {std_err}")
    # Step 3: Visualization with Error Bars for Standard Error
    plt.figure(figsize=(8, 6))
    plt.hist(sample_means, bins=30, alpha=0.7, label=f"Sample Size {size}")
    plt.errorbar(
        np.mean(sample_means), 100, xerr=std_err, fmt="o", color="black", label="±1 SE"
    )
    plt.title(f"Distribution of Sample Means (Sample Size {size}) with ±1 SE")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.legend()

plt.show()

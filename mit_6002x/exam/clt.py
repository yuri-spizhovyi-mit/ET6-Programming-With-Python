import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Parameters
sample_sizes = [1, 5, 30, 100]  # Different sample sizes to observe CLT effect
num_experiments = 1000

# Prepare plot
plt.figure(figsize=(14, 10))

for idx, size in enumerate(sample_sizes, 1):
    sample_means = []

    # Generate sample means from a highly skewed distribution (exponential)
    for _ in range(num_experiments):
        sample = np.random.exponential(scale=2.0, size=size)
        sample_means.append(np.mean(sample))

    # Plot histogram of sample means
    plt.subplot(2, 2, idx)
    sns.histplot(sample_means, kde=True, color="skyblue", bins=30)
    plt.title(f"Sample Size = {size}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.grid(True)

plt.suptitle("Central Limit Theorem: Distribution of Sample Means", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Confidence interval from last sample set
last_means = np.array(sample_means)
mean_estimate = np.mean(last_means)
std_error = np.std(last_means, ddof=1)
ci_95 = (mean_estimate - 1.96 * std_error, mean_estimate + 1.96 * std_error)

# Output estimated mean and 95% confidence interval
confidence_df = pd.DataFrame(
    {
        "Estimated Mean": [mean_estimate],
        "Standard Error": [std_error],
        "95% CI Lower Bound": [ci_95[0]],
        "95% CI Upper Bound": [ci_95[1]],
    }
)
print(confidence_df)

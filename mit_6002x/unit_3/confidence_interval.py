import numpy as np
import math
from scipy import stats

# Set seed for reproducibility
np.random.seed(42)


# ---------- 1. Confidence Interval for Sample Mean ----------
def ci_sample_mean(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)
    margin = stats.norm.ppf((1 + confidence) / 2) * (sd / np.sqrt(n))
    return mean, margin, (mean - margin, mean + margin)


# Simulate data with mean ~70, sd = 10
sample_data = np.random.normal(loc=70, scale=10, size=50)
mean, margin, ci = ci_sample_mean(sample_data)
print("🔹 Confidence Interval for Sample Mean:")
print(f"Mean = {mean:.2f}, Margin of Error = ±{margin:.2f}")
print(f"95% CI = {ci}\n")


# ---------- 2. Confidence Interval for Sample Proportion ----------
def ci_sample_proportion(successes, n, confidence=0.95):
    p_hat = successes / n
    z = stats.norm.ppf((1 + confidence) / 2)
    margin = z * math.sqrt((p_hat * (1 - p_hat)) / n)
    return p_hat, margin, (p_hat - margin, p_hat + margin)


# Example: 600 out of 1000 voters support Candidate A
p_hat, margin, ci = ci_sample_proportion(600, 1000)
print("🔹 Confidence Interval for Sample Proportion:")
print(f"Proportion = {p_hat:.2f}, Margin of Error = ±{margin:.2f}")
print(f"95% CI = {ci}\n")


# ---------- 3. Confidence Interval for Difference of Two Means ----------
def ci_diff_two_means(data1, data2, confidence=0.95):
    n1, n2 = len(data1), len(data2)
    mean1, mean2 = np.mean(data1), np.mean(data2)
    sd1, sd2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
    se = math.sqrt((sd1**2 / n1) + (sd2**2 / n2))
    diff = mean1 - mean2
    z = stats.norm.ppf((1 + confidence) / 2)
    margin = z * se
    return diff, margin, (diff - margin, diff + margin)


# Simulate test scores for two classes
class_A = np.random.normal(loc=75, scale=10, size=30)
class_B = np.random.normal(loc=80, scale=12, size=35)
diff, margin, ci = ci_diff_two_means(class_A, class_B)
print("🔹 Confidence Interval for Difference Between Two Means:")
print(f"Difference = {diff:.2f}, Margin of Error = ±{margin:.2f}")
print(f"95% CI = {ci}")

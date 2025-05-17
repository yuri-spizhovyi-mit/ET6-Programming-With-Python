import numpy as np
import matplotlib.pyplot as plt

# Benford's Law: Probabilities for first digits 1 through 9
digits = np.arange(1, 10)
benford_probs = np.log10(1 + 1 / digits)

# Simulate first digits according to Benford's Law
num_samples = 10000
simulated_digits = np.random.choice(digits, size=num_samples, p=benford_probs)

# Count frequencies
unique, counts = np.unique(simulated_digits, return_counts=True)
relative_freq = counts / num_samples

# Plot
plt.figure(figsize=(10, 6))
plt.bar(
    digits,
    benford_probs,
    alpha=0.6,
    label="Theoretical (Benford)",
    color="blue",
    edgecolor="black",
)
plt.bar(
    unique,
    relative_freq,
    alpha=0.6,
    label="Simulated",
    color="orange",
    edgecolor="black",
)
plt.title("Simulated Benford's Law Distribution vs Theoretical")
plt.xlabel("Leading Digit")
plt.ylabel("Relative Frequency")
plt.xticks(digits)
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.show()

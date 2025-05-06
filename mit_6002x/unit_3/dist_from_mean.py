import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = [70, 72, 68, 74, 71]
mean = np.mean(data)

# Compute deviations from the mean
deviations = [x - mean for x in data]

# Set up plot
plt.figure(figsize=(8, 4))
plt.axhline(y=0, color="gray", linestyle="--")
plt.plot([0, 1, 2, 3, 4], deviations, "ro", label="Deviations from Mean")
for i, dev in enumerate(deviations):
    plt.vlines(i, 0, dev, color="red", linestyle="--")

# Annotate points
for i, x in enumerate(data):
    plt.text(i, deviations[i] + 0.2, f"{x}", ha="center", fontsize=10)

plt.xticks(range(len(data)), [f"Point {i + 1}" for i in range(len(data))])
plt.ylabel("Deviation from Mean")
plt.title("Visualization of Deviations from the Mean")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

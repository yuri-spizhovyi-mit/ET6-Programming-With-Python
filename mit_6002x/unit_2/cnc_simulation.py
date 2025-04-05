import random
import matplotlib.pyplot as plt

# Parameters
target_length = 100.0  # in mm
tolerance = 0.0025  # ±0.0025 mm
num_parts = 100

# Simulate measured lengths using normal distribution around target length
# We'll assume that the machine's variation is well within the tolerance range
# We'll use a small standard deviation to reflect precision
simulated_lengths = [
    random.gauss(target_length, tolerance / 2) for _ in range(num_parts)
]

# Calculate mean, variance, and standard deviation
mean_length = sum(simulated_lengths) / len(simulated_lengths)
squared_diffs = [(x - target_length) ** 2 for x in simulated_lengths]
variance = sum(squared_diffs) / len(simulated_lengths)
std_dev = variance**0.5

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(simulated_lengths, "o-", label="Measured Lengths")
plt.axhline(
    target_length, color="green", linestyle="--", label=f"Target = {target_length} mm"
)
plt.fill_between(
    range(num_parts),
    target_length - std_dev,
    target_length + std_dev,
    color="green",
    alpha=0.2,
    label=f"±1 Std Dev = {std_dev:.6f} mm",
)

plt.title("CM-1 CNC: Length Deviation from Target (100 Parts)")
plt.xlabel("Part Index")
plt.ylabel("Measured Length (mm)")
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random

# Generate values
x_vals = np.array([random.random() for _ in range(1000)])
y_vals = np.array([random.random() for _ in range(1000)])
w_vals = np.array([random.random() for _ in range(1000)])

# Manipulate values
x_vals = x_vals + x_vals  # double the array
z_vals = x_vals + y_vals
t_vals = z_vals + y_vals + w_vals

# Plot histogram of tVals
plt.figure(figsize=(10, 6))
plt.hist(t_vals, bins=50, density=True, alpha=0.7, color="skyblue", edgecolor="black")
plt.title("Histogram of tVals")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()

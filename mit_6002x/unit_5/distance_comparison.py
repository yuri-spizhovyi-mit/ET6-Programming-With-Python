import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

# Define two points
A = np.array([2, 4, 5])
B = np.array([1, 1, 1])

# Calculate and store distances
p_values = np.linspace(1, 10, 100)
distances = [distance.minkowski(A, B, p) for p in p_values]

# Also compute Manhattan and Euclidean for comparison
manhattan = distance.cityblock(A, B)
euclidean = distance.euclidean(A, B)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(p_values, distances, label="Minkowski Distance", color="blue")
plt.axhline(y=manhattan, color="red", linestyle="--", label="Manhattan Distance (p=1)")
plt.axhline(
    y=euclidean, color="green", linestyle="--", label="Euclidean Distance (p=2)"
)
plt.title("Minkowski Distance for Different p Values")
plt.xlabel("p value")
plt.ylabel("Distance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Sample data: [x, y], label
data = {"A": [[1, 2], [2, 3], [3, 1]], "B": [[6, 5], [7, 7], [8, 6]]}

# The point we want to classify
new_point = [5, 5]


def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def knn_classify(data, query, k=3):
    distances = []

    for label in data:
        for point in data[label]:
            dist = euclidean_distance(point, query)
            distances.append((dist, label))

    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    labels = [label for _, label in k_nearest]

    most_common = Counter(labels).most_common(1)[0][0]
    return most_common


# Classify the new point
result = knn_classify(data, new_point, k=3)
print(f"The new point {new_point} is classified as: {result}")

# --- Visualization ---
colors = {"A": "blue", "B": "red"}
for label in data:
    x, y = zip(*data[label])
    plt.scatter(x, y, color=colors[label], label=f"Class {label}")

plt.scatter(*new_point, color="green", label="New Point", s=100, marker="*")
plt.title(f"k-NN Classification (k=3): Class {result}")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

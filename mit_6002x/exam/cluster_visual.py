import matplotlib.pyplot as plt
import numpy as np


# Re-define Example and Cluster with numpy for plotting
class Example:
    def __init__(self, name, features, label=None):
        self.name = name
        self.features = np.array(features, dtype=float)
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def get_features(self):
        return self.features.copy()

    def get_label(self):
        return self.label

    def get_name(self):
        return self.name

    def distance(self, other):
        return np.linalg.norm(self.features - other.get_features())

    def __str__(self):
        return f"{self.name}: {self.features.tolist()}: {self.label}"


class Cluster:
    def __init__(self, examples):
        self.examples = examples
        self.centroid = self.compute_centroid()

    def compute_centroid(self):
        feature_matrix = np.array([e.get_features() for e in self.examples])
        mean_features = feature_matrix.mean(axis=0)
        return Example("centroid", mean_features)

    def get_centroid(self):
        return self.centroid

    def members(self):
        return self.examples


# Create two sample clusters
cluster1 = Cluster(
    [Example("A", [1.0, 2.0]), Example("B", [1.5, 1.8]), Example("C", [1.2, 2.2])]
)

cluster2 = Cluster(
    [Example("D", [4.0, 4.0]), Example("E", [3.8, 4.2]), Example("F", [4.2, 3.8])]
)


# Plotting the clusters
def plot_clusters(clusters):
    for cluster in clusters:
        points = np.array([e.get_features() for e in cluster.members()])
        centroid = cluster.get_centroid().get_features()
        plt.scatter(points[:, 0], points[:, 1], label=f"Cluster at {centroid}")
        plt.scatter(
            centroid[0], centroid[1], marker="x", s=100, color="black"
        )  # centroid

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Cluster Visualization")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")


plot_clusters([cluster1, cluster2])
plt.show()

import numpy as np
import random


# Define Example and Cluster again for completeness
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

    def update(self, examples):
        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)

    def compute_centroid(self):
        feature_matrix = np.array([e.get_features() for e in self.examples])
        mean_features = feature_matrix.mean(axis=0)
        return Example("centroid", mean_features)

    def get_centroid(self):
        return self.centroid

    def variability(self):
        return sum((e.distance(self.centroid)) ** 2 for e in self.examples)

    def members(self):
        return self.examples

    def __str__(self):
        names = sorted(e.get_name() for e in self.examples)
        result = f"Cluster with centroid {self.centroid.get_features()} contains:\n"
        result += ", ".join(names)
        return result


# Dissimilarity function
def dissimilarity(clusters):
    return sum(c.variability() for c in clusters)


# Core k-means function
def kmeans(examples, k, verbose=False):
    initial_centroids = random.sample(examples, k)
    clusters = [Cluster([e]) for e in initial_centroids]

    converged = False
    num_iterations = 0

    while not converged:
        num_iterations += 1
        new_clusters = [[] for _ in range(k)]

        for e in examples:
            distances = [e.distance(cluster.get_centroid()) for cluster in clusters]
            closest_index = np.argmin(distances)
            new_clusters[closest_index].append(e)

        if any(len(cluster) == 0 for cluster in new_clusters):
            raise ValueError("Empty Cluster")

        converged = True
        for i in range(k):
            if clusters[i].update(new_clusters[i]) > 0.0:
                converged = False

        if verbose:
            print(f"Iteration #{num_iterations}")
            for c in clusters:
                print(c)
            print()

    return clusters


# Try multiple trials of k-means and return best
def try_kmeans(examples, num_clusters, num_trials, verbose=False):
    best_clusters = kmeans(examples, num_clusters, verbose)
    min_dissimilarity = dissimilarity(best_clusters)
    trials = 1

    while trials < num_trials:
        try:
            current_clusters = kmeans(examples, num_clusters, verbose)
        except ValueError:
            continue
        current_dissimilarity = dissimilarity(current_clusters)
        if current_dissimilarity < min_dissimilarity:
            best_clusters = current_clusters
            min_dissimilarity = current_dissimilarity
        trials += 1

    return best_clusters


# Create example dataset and run
examples = [
    Example("A", [1.0, 2.0]),
    Example("B", [1.5, 1.8]),
    Example("C", [1.2, 2.2]),
    Example("D", [4.0, 4.0]),
    Example("E", [3.8, 4.2]),
    Example("F", [4.2, 3.8]),
]

# Try KMeans
final_clusters = try_kmeans(examples, num_clusters=2, num_trials=5, verbose=False)

# Prepare results for plotting
import matplotlib.pyplot as plt


def plot_clusters(clusters):
    for cluster in clusters:
        points = np.array([e.get_features() for e in cluster.members()])
        centroid = cluster.get_centroid().get_features()
        plt.scatter(points[:, 0], points[:, 1], label=f"Cluster at {centroid}")
        plt.scatter(centroid[0], centroid[1], marker="x", s=100, color="black")

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("K-Means Cluster Result")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")


plot_clusters(final_clusters)
plt.show()

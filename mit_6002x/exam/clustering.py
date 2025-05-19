import numpy as np


# Define Minkowski Distance (p=2 means Euclidean)
def minkowski_dist(v1, v2, p):
    return sum(abs(a - b) ** p for a, b in zip(v1, v2)) ** (1 / p)


class Example:
    def __init__(self, name, features, label=None):
        # Assumes features is a list or array of floats
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
        return minkowski_dist(self.features, other.get_features(), 2)

    def __str__(self):
        return f"{self.name}: {self.features.tolist()}: {self.label}"


class Cluster:
    def __init__(self, examples):
        """Assumes examples is a non-empty list of Example instances"""
        self.examples = examples
        self.centroid = self.compute_centroid()

    def update(self, examples):
        """Update examples and return how much the centroid moved"""
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


# Example usage
if __name__ == "__main__":
    e1 = Example("A", [1.0, 2.0])
    e2 = Example("B", [2.0, 3.0])
    e3 = Example("C", [1.5, 2.5])
    cluster = Cluster([e1, e2, e3])

    print(cluster)
    print(f"Variability: {cluster.variability():.2f}")

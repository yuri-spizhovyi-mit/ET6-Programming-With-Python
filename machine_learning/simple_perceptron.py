import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Define a simple dataset (AND gate-like)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Only (1,1) gives 1 like AND


# Perceptron implementation with weight updates
class SimplePerceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs
        self.history = []

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Add bias term
        return self.activation(np.dot(self.weights, x_with_bias))

    def train(self, X, y):
        for epoch in range(self.epochs):
            for xi, target in zip(X, y):
                xi_with_bias = np.insert(xi, 0, 1)
                output = self.predict(xi)
                error = target - output
                self.weights += self.lr * error * xi_with_bias
            self.history.append(self.weights.copy())


# Train the perceptron
p = SimplePerceptron(input_size=2, learning_rate=0.2, epochs=10)
p.train(X, y)

# Prepare meshgrid for decision boundary visualization
x_min, x_max = -0.1, 1.1
y_min, y_max = -0.1, 1.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
Z = np.array([p.predict([x1, x2]) for x1, x2 in zip(xx.ravel(), yy.ravel())])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.figure(figsize=(6, 6))
plt.contourf(xx, yy, Z, cmap=ListedColormap(["#FFCCCC", "#CCFFCC"]), alpha=0.6)
plt.scatter(
    X[:, 0], X[:, 1], c=y, cmap=ListedColormap(["red", "green"]), edgecolors="k", s=100
)
plt.title("Perceptron Decision Boundary (Learned from Data)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.show()

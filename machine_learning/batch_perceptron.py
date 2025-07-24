import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

# --- Step 1: Create training data (AND gate) ---
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])


# --- Step 2: Batch Perceptron Class ---
class BatchPerceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs
        self.history = []

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)
        return self.activation(np.dot(self.weights, x_with_bias))

    def train(self, X, y):
        for _ in range(self.epochs):
            total_update = np.zeros_like(self.weights)
            for xi, target in zip(X, y):
                xi_with_bias = np.insert(xi, 0, 1)
                output = self.predict(xi)
                error = target - output
                total_update += self.lr * error * xi_with_bias
            self.weights += total_update
            self.history.append(self.weights.copy())


# --- Step 3: Train Perceptron ---
p = BatchPerceptron(input_size=2, learning_rate=0.2, epochs=10)
p.train(X, y)

# --- Step 4: Setup for Animation ---
x_min, x_max = -0.1, 1.1
y_min, y_max = -0.1, 1.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))

fig, ax = plt.subplots(figsize=(6, 6))


def update(epoch):
    ax.clear()
    weights = p.history[epoch]
    Z = np.array(
        [
            1 if (weights[0] + weights[1] * x1 + weights[2] * x2) >= 0 else 0
            for x1, x2 in zip(xx.ravel(), yy.ravel())
        ]
    ).reshape(xx.shape)

    ax.contourf(xx, yy, Z, cmap=ListedColormap(["#FFCCCC", "#CCFFCC"]), alpha=0.6)
    ax.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        cmap=ListedColormap(["red", "green"]),
        edgecolors="k",
        s=100,
    )
    ax.set_title(f"Batch Training - Epoch {epoch + 1}")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.grid(True)


ani = FuncAnimation(fig, update, frames=len(p.history), interval=800, repeat=False)
plt.show()

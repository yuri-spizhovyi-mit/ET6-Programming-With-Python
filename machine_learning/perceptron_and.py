import numpy as np
# AND gate inputs and expected outputs
# x1  x2  =>  y
# 0   0   =>  0
# 0   1   =>  0
# 1   0   =>  0
# 1   1   =>  1

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

y = np.array([0, 0, 0, 1])  # Target output


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0  # Step function

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Add bias input = 1
        weighted_sum = np.dot(self.weights, x_with_bias)
        return self.activation(weighted_sum)

    def train(self, X, y):
        for epoch in range(self.epochs):
            for xi, target in zip(X, y):
                xi_with_bias = np.insert(xi, 0, 1)  # Add bias
                prediction = self.predict(xi)
                error = target - prediction
                self.weights += self.lr * error * xi_with_bias
            print(f"Epoch {epoch + 1} - Weights: {self.weights}")


# Initialize and train
perceptron = Perceptron(input_size=2)
perceptron.train(X, y)

print("\nPredictions:")
for x in X:
    print(f"{x} => {perceptron.predict(x)}")

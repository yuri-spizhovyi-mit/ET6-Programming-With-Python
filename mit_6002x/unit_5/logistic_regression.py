import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=42,
)

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Predict on a sample point
new_point = np.array([[0, 0]])
prediction = model.predict(new_point)
print(f"Predicted class for {new_point[0]}: {prediction[0]}")

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="bwr", edgecolor="k", label="Data Points")
plt.scatter(
    new_point[0, 0],
    new_point[0, 1],
    c="gold",
    edgecolor="black",
    marker="*",
    s=200,
    label="New Point",
)

# Draw decision boundary
x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_values = -(model.coef_[0][0] * x_values + model.intercept_[0]) / model.coef_[0][1]
plt.plot(x_values, y_values, color="black", linestyle="--", label="Decision Boundary")

plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()

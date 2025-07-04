# Step 1: Import Libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 2: Sample Data
# X = House sizes in square feet
# y = Prices in $1000s
X = np.array([[600], [800], [1000], [1200], [1500]])  # feature (2D)
y = np.array([150, 200, 250, 300, 375])  # target (1D)

# Step 3: Create and Train the Model
model = LinearRegression()
model.fit(X, y)

# Step 4: Make Predictions
size_to_predict = np.array([[1100]])  # example size
predicted_price = model.predict(size_to_predict)

print(f"Predicted price for 1100 sq ft = ${predicted_price[0] * 1000:.2f}")

# Step 5: Visualization (Optional)
plt.scatter(X, y, color="black", label="Training data")
plt.plot(X, model.predict(X), color="blue", label="Regression line")
plt.scatter(size_to_predict, predicted_price, color="red", label="Prediction")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("Linear Regression: House Price Prediction")
plt.legend()
plt.show()

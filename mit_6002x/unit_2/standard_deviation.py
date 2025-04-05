import matplotlib.pyplot as plt

# Example data
data = [5, 7, 9, 4, 6, 8, 5, 7, 10, 6]

# Step-by-step calculation of variance and std deviation
mean = sum(data) / len(data)
squared_diffs = [(x - mean) ** 2 for x in data]
variance = sum(squared_diffs) / len(data)
std_dev = variance**0.5

# Plotting the data and visualizing the mean and standard deviation
plt.figure(figsize=(10, 6))
plt.plot(data, "o-", label="Data Points")
plt.axhline(mean, color="orange", linestyle="--", label=f"Mean = {mean:.2f}")
plt.fill_between(
    range(len(data)),
    mean - std_dev,
    mean + std_dev,
    color="orange",
    alpha=0.2,
    label=f"±1 Std Dev = {std_dev:.2f}",
)

plt.title("Visualization of Mean and Standard Deviation")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

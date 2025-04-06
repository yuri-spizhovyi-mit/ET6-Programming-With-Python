import math
import pylab as plt


data = []
x_vals = range(1, 10)
for d in x_vals:
    result = math.log((1 + 1 / d), 10) * 100
    data.append(result)


# Plot line with triangle markers
plt.plot(
    x_vals, data, label="Probability of the non-zero digit", marker="o", color="blue"
)

# Add label to each marker
for x, y in zip(x_vals, data):
    plt.text(x, y + 0.5, f"{y:.1f}%", fontsize=8)


plt.xlabel("Non-zero digit")
plt.ylabel("Probability of appearence first, %")
plt.title("Probability of appearance non-zero digit first")
# Add thin gray grid lines
plt.grid(True, which="both", color="gray", linestyle="--", linewidth=0.5)
plt.show()

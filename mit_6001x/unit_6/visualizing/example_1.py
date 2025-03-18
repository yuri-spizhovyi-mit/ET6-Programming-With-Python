import pylab as plt

my_samples = []
my_linear = []
my_quadratic = []
my_cubic = []
my_exponential = []

for i in range(0, 30):
    my_samples.append(i)
    my_linear.append(i)
    my_quadratic.append(i**2)
    my_cubic.append(i**3)
    my_exponential.append(1.5**i)

plt.plot(my_samples, my_linear, label="Linear")
plt.plot(my_samples, my_quadratic, label="Quadratic")
plt.plot(my_samples, my_cubic, label="Cubic")
plt.plot(my_samples, my_exponential, label="Exponential")

plt.legend()  # Optional, to see labels
plt.xlabel("Samples")
plt.ylabel("Values")
plt.title("Different Growth Rates")
plt.show()  # 🔥 This line is what shows the plot window

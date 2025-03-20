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

plt.figure("cube exp log")
plt.clf()
plt.plot(my_samples, my_cubic, "g^", label="Cubic", linewidth=4.0)
plt.plot(my_samples, my_exponential, "r--", label="Exponential", linewidth=5.0)
plt.yscale("log")
plt.legend()
plt.title("Cubic vs. Exponential")


plt.figure("cube exp linear")
plt.clf()
plt.plot(my_samples, my_cubic, "g--", label="cubic", linewidth=2.0)
plt.plot(my_samples, my_exponential, "r", label="exponential", linewidth=4.0)
plt.legend()
plt.title("Cubic vs. Exponential")

plt.show()

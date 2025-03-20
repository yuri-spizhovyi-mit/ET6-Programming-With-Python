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

plt.figure("linear quad")

plt.clf()
plt.ylim(0, 20000)
plt.xlabel("Sample points")
plt.ylabel("linear function")
plt.title("Different Growth Rates")
plt.plot(my_samples, my_linear, label="Linear")
plt.plot(my_samples, my_quadratic, label="Quadratic")
plt.plot(my_samples, my_cubic, label="Cubic")
plt.plot(my_samples, my_exponential, label="Exponential")
plt.legend(loc="upper left")
plt.figure("quad")
plt.legend()
plt.clf()
plt.ylim(0, 1000)
plt.xlabel("Sample points")
plt.ylabel("quad function")
plt.title("Different Growth Rates")
plt.plot(my_samples, my_quadratic, label="Quadratic")
plt.legend()
plt.figure("cube")
plt.clf()
plt.ylim(0, 1000)
plt.plot(my_samples, my_cubic, label="Cubic")
plt.legend()
plt.figure("expo")
plt.clf()
plt.ylim(0, 1000)
plt.plot(my_samples, my_exponential, label="Exponential")

plt.legend()  # Optional, to see labels
plt.xlabel("Samples")
plt.ylabel("Values")
plt.title("Different Growth Rates")
plt.show()  # 🔥 This line is what shows the plot window

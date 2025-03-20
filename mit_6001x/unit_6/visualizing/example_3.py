import pylab as plt
from samples import my_samples, my_cubic, my_exponential

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

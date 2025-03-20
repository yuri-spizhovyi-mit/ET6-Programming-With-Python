import pylab as plt
from samples import my_samples, my_linear, my_quadratic, my_cubic, my_exponential

plt.figure("lin quad")
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(my_samples, my_linear, "b-", label="Linear", linewidth=2.0)
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(my_samples, my_quadratic, "ro", label="Quadratic", linewidth=3.0)
plt.legend(loc="upper left")
plt.title("Linears vs. Quadratic")

plt.figure("cube exp")
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(my_samples, my_cubic, "g^", label="Cubic", linewidth=4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(my_samples, my_exponential, "r--", label="Exponential", linewidth=5.0)
plt.legend()
plt.title("Cubic vs. Exponential")

plt.show()  # 🔥 This line is what shows the plot window

from matplotlib_venn import venn2
import matplotlib.pyplot as plt

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6}

venn2([A, B], set_labels=("Set A", "Set B"))
plt.show()

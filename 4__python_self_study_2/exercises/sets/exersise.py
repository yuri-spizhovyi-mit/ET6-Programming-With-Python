import matplotlib.pyplot as plt
from matplotlib_venn import venn3

Z = [10, 1, 2]
X = [3, 4]
Q = Z + X
print("Q equal: ", Q)

A = {1, 2, 3}
B = {1, 2, 4}
C = {1, 2, 10}

result = (A - B).union(C - B)
print("Result:", result)

# Create the Venn diagram
venn = venn3([A, B, C], ("Set A", "Set B", "Set C"))

# Highlight only the result on the Venn diagram
venn.get_label_by_id("100").set_text("\n".join(map(str, A - B)))  # A - B
venn.get_label_by_id("001").set_text("\n".join(map(str, C - B)))  # C - B

# Clear other labels to focus on (A - B) ∪ (C - B)
for subset in ("010", "110", "101", "011", "111"):
    if venn.get_label_by_id(subset):
        venn.get_label_by_id(subset).set_text("")

# Add a title explaining the operation being visualized
plt.title("Venn Diagram for (A - B) ∪ (C - B)")
plt.show()

"""
Venn Diagram Visualization
Customer Overlap Analysis
Analyze customer overlap between two e-commerce platforms.
"""
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
platform_A_customers = {"Alice", "Bob", "Charlie"}
platform_B_customers = {"Charlie", "Dave", "Eve"}
venn2([platform_A_customers, platform_B_customers], ("Platform A", "Platform B"))
plt.show()

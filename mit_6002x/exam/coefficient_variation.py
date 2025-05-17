"""Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places"""

import numpy as np

# Data
data = np.array([10, 4, 12, 15, 20, 5])

# Calculate mean and standard deviation

mean_val = np.mean(data)
std_dev = np.std(data, ddof=0)  # Population standard deviation

# Coefficient of Variation (CV)

cv = std_dev / mean_val

# Round to 3 decimal point
cv_rounded = round(cv, 3)
print(cv_rounded, mean_val, std_dev)

import numpy as np

# A small dataset (e.g., test scores)
data = [70, 72, 68, 74, 71]

# Population standard deviation (ddof=0)
pop_sd = np.std(data, ddof=0)

# Sample standard deviation (ddof=1)
sample_sd = np.std(data, ddof=1)

print("Data:", data)
print("Population Standard Deviation (ddof=0):", round(pop_sd, 2))
print("Sample Standard Deviation (ddof=1):", round(sample_sd, 2))

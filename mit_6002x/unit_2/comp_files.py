import os
import math
import matplotlib.pyplot as plt
from collections import Counter


def get_first_digit(n):
    while n >= 10:
        n //= 10
    return n


# 📁 Scan all files in a folder and get their sizes
def collect_file_sizes(folder):
    sizes = []
    for dirpath, _, filenames in os.walk(folder):
        for file in filenames:
            try:
                full_path = os.path.join(dirpath, file)
                size = os.path.getsize(full_path)
                if size > 0:
                    sizes.append(get_first_digit(size))
            except Exception as e:
                continue
    return sizes


# Change this path to a folder you want to scan

# folder_path = "."  # current folder
folder_path = "C:/Windows"
first_digits = collect_file_sizes(folder_path)

# Count how often each digit 1–9 appears as first digit
counted = Counter(first_digits)
total = sum(counted.values())
digit_freq = [100 * counted[d] / total if d in counted else 0 for d in range(1, 10)]

# Expected Benford values
benford = [math.log10(1 + 1 / d) * 100 for d in range(1, 10)]

# Plotting
digits = list(range(1, 10))
plt.bar(digits, digit_freq, width=0.4, label="Your Files", align="center")
plt.plot(digits, benford, "ro--", label="Benford's Law")
plt.xlabel("First Digit")
plt.ylabel("Frequency (%)")
plt.title("First Digit Distribution of File Sizes")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.xticks(digits)
plt.show()

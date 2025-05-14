import numpy as np


def i_scale_features(vals):
    vals = np.array(vals, dtype=float)
    min_val = np.min(vals)
    max_val = np.max(vals)
    return (vals - min_val) / (max_val - min_val)


# Example
original = [10, 20, 30, 40, 50]
i_scaled = i_scale_features(original)

print("Original:", original)
print("Interpolated (0–1):", np.round(i_scaled, 3))

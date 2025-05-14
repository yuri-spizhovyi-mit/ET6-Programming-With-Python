import numpy as np


def z_scale_features(vals):
    vals = np.array(vals, dtype=float)
    mean = np.mean(vals)
    std = np.std(vals)
    return (vals - mean) / std


# Example
original = [10, 20, 30, 40, 50]
z_scaled = z_scale_features(original)

print("Original:", original)
print("Z-scaled:", np.round(z_scaled, 3))

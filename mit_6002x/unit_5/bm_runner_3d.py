from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
import numpy as np
import csv

import matplotlib.pyplot as plt


def load_and_parse_runners(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        ages, times, genders = [], [], []
        for row in reader:
            ages.append(int(row["age"]))
            times.append(float(row["time"]))
            genders.append(row["gender"])
    return ages, times, genders


# Load data
ages, times, genders = load_and_parse_runners("boston_marathon_100.csv")
# Prepare data
ages_np = np.array(ages)
times_np = np.array(times)
genders_np = np.array([1 if g == "female" else 0 for g in genders])  # female=1, male=0

# Create 3D Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
scatter = ax.scatter(ages_np, times_np, genders_np, c=genders_np, cmap="coolwarm", s=50)

ax.set_xlabel("Age")
ax.set_ylabel("Finish Time (minutes)")
ax.set_zlabel("Gender (0 = male, 1 = female)")
ax.set_title("3D View of Runners by Age, Time, and Gender")
plt.tight_layout()
plt.show()

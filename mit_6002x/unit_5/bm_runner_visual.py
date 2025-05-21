import csv

import matplotlib.pyplot as plt


# Load the expanded dataset
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

# Plotting
plt.figure(figsize=(10, 6))
for age, time, gender in zip(ages, times, genders):
    color = "red" if gender == "female" else "blue"
    marker = "o" if gender == "female" else "s"
    plt.scatter(
        age,
        time,
        color=color,
        marker=marker,
        label=gender if gender not in plt.gca().get_legend_handles_labels()[1] else "",
    )

plt.xlabel("Age")
plt.ylabel("Finish Time (minutes)")
plt.title("Boston Marathon Runners: Age vs. Finish Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

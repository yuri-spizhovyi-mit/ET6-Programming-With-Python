# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:45:20 2016

Updated for Python 3 and PEP8 compliance
"""

import matplotlib.pyplot as plt
import numpy as np

# Global plot style settings
plt.rcParams["lines.linewidth"] = 4
plt.rcParams["axes.titlesize"] = 20
plt.rcParams["axes.labelsize"] = 20
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
plt.rcParams["xtick.major.size"] = 7
plt.rcParams["ytick.major.size"] = 7
plt.rcParams["lines.markersize"] = 10
plt.rcParams["legend.numpoints"] = 1


def minkowski_distance(v1, v2, p):
    """Returns Minkowski distance of order p between two vectors."""
    return sum(abs(a - b) ** p for a, b in zip(v1, v2)) ** (1 / p)


class Animal:
    def __init__(self, name, features):
        self.name = name
        self.features = np.array(features)

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    def distance(self, other):
        return minkowski_distance(self.features, other.features, 2)

    def __str__(self):
        return self.name


# Create animal instances
animals = [
    Animal("cobra", [1, 1, 1, 1, 0]),
    Animal("rattlesnake", [1, 1, 1, 1, 0]),
    Animal("boa constrictor", [0, 1, 0, 1, 0]),
    Animal("chicken", [1, 1, 0, 1, 2]),
    Animal("alligator", [1, 1, 0, 1, 4]),
    Animal("dart frog", [1, 0, 1, 0, 4]),
    Animal("salmon", [1, 1, 0, 1, 0]),
    Animal("python", [1, 1, 0, 1, 0]),
]


def compare_animals(animal_list, precision=3):
    """Builds and displays a table of Euclidean distances between animals."""
    names = [animal.get_name() for animal in animal_list]
    table_data = []

    for animal1 in animal_list:
        row = []
        for animal2 in animal_list:
            if animal1 == animal2:
                row.append("--")
            else:
                distance = round(animal1.distance(animal2), precision)
                row.append(str(distance))
        table_data.append(row)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")

    table = plt.table(
        cellText=table_data,
        rowLabels=names,
        colLabels=names,
        cellLoc="center",
        loc="center",
        colWidths=[0.2] * len(animal_list),
        bbox=[0, 0, 1, 1],
    )

    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 2.5)

    plt.tight_layout()
    plt.savefig("distances.png")
    plt.show()


# Generate and display the table
compare_animals(animals)

# Print distances in readable format
for idx1 in range(len(animals)):
    for idx2 in range(idx1 + 1, len(animals)):
        first_animal = animals[idx1]
        second_animal = animals[idx2]
        dist_value = round(first_animal.distance(second_animal), 3)
        print(f"Distance between {first_animal} and {second_animal} is {dist_value}")

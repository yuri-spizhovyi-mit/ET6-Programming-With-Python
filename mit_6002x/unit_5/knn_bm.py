import csv
import random


# Updated version with Python 3 naming conventions (snake_case)
class Runner:
    def __init__(self, gender, age, time):
        self.feature_vec = (age, time)
        self.label = gender

    def feature_dist(self, other):
        return (
            sum((a - b) ** 2 for a, b in zip(self.feature_vec, other.feature_vec))
            ** 0.5
        )

    def get_time(self):
        return self.feature_vec[1]

    def get_age(self):
        return self.feature_vec[0]

    def get_label(self):
        return self.label

    def get_features(self):
        return self.feature_vec

    def __str__(self):
        return f"{self.get_age()}, {self.get_time()}, {self.label}"


def load_marathon_data(file_name):
    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = {"gender": [], "age": [], "time": []}
        for row in reader:
            data["gender"].append(row["gender"])
            data["age"].append(int(row["age"]))
            data["time"].append(float(row["time"]))
    return data


def build_marathon_examples(file_name):
    data = load_marathon_data(file_name)
    examples = [
        Runner(data["gender"][i], data["age"][i], data["time"][i])
        for i in range(len(data["age"]))
    ]
    return examples


def split_80_20(examples):
    sample_indices = random.sample(range(len(examples)), len(examples) // 5)
    training_set = [
        examples[i] for i in range(len(examples)) if i not in sample_indices
    ]
    test_set = [examples[i] for i in sample_indices]
    return training_set, test_set


def find_k_nearest(example, example_set, k):
    distances = [(e, example.feature_dist(e)) for e in example_set]
    distances.sort(key=lambda x: x[1])
    return [d[0] for d in distances[:k]]


def knn_classify(training_set, test_set, target_label, k):
    true_pos = false_pos = true_neg = false_neg = 0
    for example in test_set:
        nearest = find_k_nearest(example, training_set, k)
        matches = sum(1 for neighbor in nearest if neighbor.get_label() == target_label)
        if matches > k // 2:
            if example.get_label() == target_label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if example.get_label() != target_label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


# Test with updated variable names
file_path = "boston_marathon_mock.csv"
examples = build_marathon_examples(file_path)
training_set, test_set = split_80_20(examples)
results = knn_classify(training_set, test_set, "female", 3)
print(results)

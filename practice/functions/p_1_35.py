import random
import matplotlib.pyplot as plt


def birthday_paradox(n, num_trials):
    """Return the probability that at least two people out of n share a birthday."""
    matches = 0
    for _ in range(num_trials):
        birthdays = set()
        for _ in range(n):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                matches += 1
                break
            birthdays.add(birthday)
    return matches / num_trials


def plot_birthday_probabilities(max_n=100, num_trials=1000):
    """Plot the probability of shared birthdays for group sizes from 2 to max_n."""
    x_vals = list(range(2, max_n + 1))
    y_vals = [birthday_paradox(n, num_trials) for n in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, marker='o')
    plt.axhline(y=0.5, color='red', linestyle='--', label='50% Probability')
    plt.title("Birthday Paradox: Probability of Shared Birthday")
    plt.xlabel("Number of People in Room (n)")
    plt.ylabel("Probability")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"Probability with 23 people: {birthday_paradox(23, 10000):.4f}")
    plot_birthday_probabilities()

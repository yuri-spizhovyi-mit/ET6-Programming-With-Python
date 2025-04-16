import random
import matplotlib.pyplot as plt


class SeriesSimulator:
    def __init__(self, num_series, series_length=7):
        self.num_series = num_series
        self.series_length = series_length

    def play_series(self, team_prob):
        """
        Simulates a single series and returns True if the team wins the series.
        """
        num_won = 0
        for _ in range(self.series_length):
            if random.random() <= team_prob:
                num_won += 1
        return num_won > self.series_length // 2

    def fraction_won(self, team_prob):
        """
        Simulates multiple series and returns the fraction of series won.
        """
        won = 0
        for _ in range(self.num_series):
            if self.play_series(team_prob):
                won += 1
        return won / self.num_series

    def run_simulation(self):
        """
        Runs the full simulation over a range of team probabilities and visualizes results.
        """
        probs = []
        fracs_won = []
        prob = 0.5

        while prob <= 1.0:
            fracs_won.append(self.fraction_won(prob))
            probs.append(prob)
            prob = round(prob + 0.01, 2)  # Avoid floating-point issues

        # Plotting
        plt.axhline(0.95, color="gray", linestyle="--")
        plt.plot(probs, fracs_won, "k", linewidth=2)
        plt.xlabel("Probability of Winning a Game")
        plt.ylabel("Probability of Winning a Series")
        plt.title(f"{self.num_series} Simulated {self.series_length}-Game Series")
        plt.grid(True)
        plt.show()


def main():
    simulator = SeriesSimulator(num_series=400)
    simulator.run_simulation()


if __name__ == "__main__":
    main()

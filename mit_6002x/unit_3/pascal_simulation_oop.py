import random


class Die:
    def roll_die(self):
        return random.choice([1, 2, 3, 4, 5, 6])


class PascalGame:
    def __init__(self, num_trials):
        if num_trials <= 0:
            raise ValueError("Number of trials must be positive")
        self.num_trials = num_trials
        self.die1 = Die()
        self.die2 = Die()

    def run_simulation(self):
        num_wins = 0
        for _ in range(self.num_trials):
            for _ in range(24):
                d1 = self.die1.roll_die()
                d2 = self.die2.roll_die()
                if d1 == 6 and d2 == 6:
                    num_wins += 1
                    break
        probability = num_wins / self.num_trials
        print("Probability of winning = ", probability)


game = PascalGame(1000)
game.run_simulation()

import random
import matplotlib.pyplot as plt

def simulate_golf_rounds(average_strokes_per_hole=5, holes=9, simulations=1000):
    first_half = []
    second_half = []

    for _ in range(simulations):
        # Simulate strokes for each hole using normal distribution (mean 5, std dev 1)
        first_9 = [random.gauss(average_strokes_per_hole, 1) for _ in range(holes)]
        second_9 = [random.gauss(average_strokes_per_hole, 1) for _ in range(holes)]

        total_first_9 = sum(first_9)
        total_second_9 = sum(second_9)

        first_half.append(total_first_9)
        second_half.append(total_second_9)

    return first_half, second_half

# Simulate
first_half_strokes, second_half_strokes = simulate_golf_rounds()

# Show a scatter plot to demonstrate regression to the mean
plt.figure(figsize=(10, 6))
plt.scatter(first_half_strokes, second_half_strokes, alpha=0.3)
plt.axhline(y=45, color='gray', linestyle='--', label='Expected Mean (45)')
plt.axvline(x=45, color='gray', linestyle='--')
plt.xlabel("Strokes on First 9 Holes")
plt.ylabel("Strokes on Second 9 Holes")
plt.title("Sally's Golf Rounds: First 9 vs Second 9 (Regression to the Mean)")
plt.legend()
plt.grid(True)
plt.show()

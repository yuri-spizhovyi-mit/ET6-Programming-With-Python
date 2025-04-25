import matplotlib.pyplot as plt


def get_fib_sequence(n):
    if n <= 0:
        return []

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


fib_sequence = get_fib_sequence(20)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(range(len(fib_sequence)), fib_sequence, marker="o")
plt.title("Fibonacci Sequence (First 20 Numbers")
plt.xlabel("Index (n)")
plt.ylabel("Fibonacci Number")
plt.grid(True)
plt.show()

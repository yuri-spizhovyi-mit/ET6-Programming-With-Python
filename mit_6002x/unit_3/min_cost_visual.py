import matplotlib.pyplot as plt


def plot_min_cost_path(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    trace = [0] * (n + 1)

    for i in range(2, n + 1):
        if dp[i - 1] + cost[i - 1] < dp[i - 2] + cost[i - 2]:
            dp[i] = dp[i - 1] + cost[i - 1]
            trace[i] = i - 1
        else:
            dp[i] = dp[i - 2] + cost[i - 2]
            trace[i] = i - 2

    # Reconstruct the path
    path = []
    i = n
    while i > 0:
        path.append(i)
        i = trace[i]
    path.reverse()

    # Plot
    steps = list(range(len(cost)))
    plt.figure(figsize=(10, 5))
    plt.bar(steps, cost, color="lightgray", edgecolor="black")
    plt.xticks(steps)
    plt.xlabel("Step Index")
    plt.ylabel("Cost")
    plt.title("Cost per Step and Path Taken to Reach the Top")

    # Highlight the chosen steps
    chosen_steps = [p - 1 for p in path if p - 1 >= 0]
    for step in chosen_steps:
        plt.bar(step, cost[step], color="lightgreen", edgecolor="black")

    plt.show()


# Use the second example from the problem
plot_min_cost_path([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

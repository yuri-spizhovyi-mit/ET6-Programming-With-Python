import pylab  # from matplotlib.pylab, includes numpy functions


def r_squared(measured, predicted):
    """Compute the coefficient of determination (R²)"""
    estimate_error = ((predicted - measured) ** 2).sum()
    mean_of_measured = measured.sum() / len(measured)
    variability = ((measured - mean_of_measured) ** 2).sum()
    return 1 - estimate_error / variability


def get_trajectory_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()[1:]  # Skip header

    distances = []
    heights = [[] for _ in range(4)]  # Create 4 empty lists for trials

    for line in lines:
        d, *h = map(float, line.split())
        distances.append(d)
        for i in range(4):
            heights[i].append(h[i])

    return distances, heights


def process_trajectories(filename):
    distances, heights = get_trajectory_data(filename)
    num_trials = len(heights)
    distances = pylab.array(distances)

    # Compute mean height for each distance
    total_heights = pylab.zeros(len(distances))
    for trial_heights in heights:
        total_heights += pylab.array(trial_heights)
    mean_heights = total_heights / num_trials

    # Plot settings
    pylab.figure(figsize=(10, 6))
    pylab.title(f"Trajectory of Projectile (Mean of {num_trials} Trials)")
    pylab.xlabel("Inches from Launch Point")
    pylab.ylabel("Inches Above Launch Point")
    pylab.plot(distances, mean_heights, "ko", label="Mean Height")

    # Linear fit and R²
    linear_fit = pylab.polyfit(distances, mean_heights, 1)
    linear_preds = pylab.polyval(linear_fit, distances)
    pylab.plot(distances, linear_preds, "b-", label="Linear Fit")
    print("R² of linear fit =", r_squared(mean_heights, linear_preds))

    # Quadratic fit and R²
    quad_fit = pylab.polyfit(distances, mean_heights, 2)
    quad_preds = pylab.polyval(quad_fit, distances)
    pylab.plot(distances, quad_preds, "k:", label="Quadratic Fit")
    print("R² of quadratic fit =", r_squared(mean_heights, quad_preds))

    pylab.legend()
    pylab.grid(True)
    pylab.show()


process_trajectories(
    "C:/Users/yspizhoviy/ET6-Programming-With-Python/mit_6002x/unit_4/launcherData.txt"
)

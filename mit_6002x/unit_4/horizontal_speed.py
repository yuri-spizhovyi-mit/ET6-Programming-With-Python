import pylab


def get_trajectory_data(filename):
    """Loads projectile data from file and returns distances and 4 height lists."""
    with open(filename, "r") as file:
        lines = file.readlines()[1:]  # Skip header

    distances = []
    heights = [[] for _ in range(4)]

    for line in lines:
        d, *h = map(float, line.split())
        distances.append(d)
        for i in range(4):
            heights[i].append(h[i])

    return pylab.array(distances), heights


def compute_mean_heights(heights):
    """Computes mean heights at each distance across all trials."""
    total = pylab.zeros(len(heights[0]))
    for trial in heights:
        total += pylab.array(trial)
    return total / len(heights)


def get_horizontal_speed(quad_fit, min_x, max_x):
    """
    Calculates horizontal speed of a projectile based on quadratic fit.
    Returns horizontal speed in feet per second (rounded).
    """
    inches_per_foot = 12
    g = 32.16 * inches_per_foot  # gravity in inches/sec²

    x_mid = (max_x + min_x) / 2
    a, b, c = quad_fit
    y_peak = a * x_mid**2 + b * x_mid + c

    if y_peak <= 0:
        raise ValueError(
            f"Invalid trajectory: y_peak = {y_peak:.2f}. It must be positive."
        )

    t = (2 * y_peak / g) ** 0.5
    speed = x_mid / (t * inches_per_foot)
    return round(speed)


# === Main execution ===

# Load data
filename = "launcherData.txt"
distances, height_trials = get_trajectory_data(filename)
mean_heights = compute_mean_heights(height_trials)

# Fit a quadratic model
quad_fit = pylab.polyfit(distances, mean_heights, 2)

# Get min and max x (distance)
min_x = distances.min()
max_x = distances.max()

# Compute horizontal speed
try:
    speed = get_horizontal_speed(quad_fit, min_x, max_x)
    print(f"Horizontal speed = {speed} feet/sec")
except ValueError as e:
    print("Error:", e)

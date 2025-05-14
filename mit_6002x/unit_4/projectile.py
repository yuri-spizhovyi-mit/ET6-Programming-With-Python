import pylab  # Assumes pylab is configured as part of matplotlib


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

    # Compute mean heights at each distance
    total_heights = pylab.zeros(len(distances))
    for trial_heights in heights:
        total_heights += pylab.array(trial_heights)
    mean_heights = total_heights / num_trials

    # Plotting
    pylab.figure(figsize=(10, 6))
    pylab.title(f"Trajectory of Projectile (Mean of {num_trials} Trials)")
    pylab.xlabel("Inches from Launch Point")
    pylab.ylabel("Inches Above Launch Point")
    pylab.plot(distances, mean_heights, "ko", label="Mean Height")

    # Linear Fit
    linear_fit = pylab.polyfit(distances, mean_heights, 1)
    pylab.plot(
        distances, pylab.polyval(linear_fit, distances), "b-", label="Linear Fit"
    )

    # Quadratic Fit
    quad_fit = pylab.polyfit(distances, mean_heights, 2)
    pylab.plot(
        distances, pylab.polyval(quad_fit, distances), "k:", label="Quadratic Fit"
    )

    pylab.legend()
    pylab.grid(True)
    pylab.show()


# Run the trajectory analysis
process_trajectories("launcherData.txt")

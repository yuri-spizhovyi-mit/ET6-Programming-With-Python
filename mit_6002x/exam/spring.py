import pylab as plt


def get_data(file_name):
    distances = []
    masses = []
    with open(file_name, "r") as f:
        next(f)  # Skip header
        for line in f:
            d, m = line.strip().split()
            distances.append(float(d))
            masses.append(float(m))
    return plt.array(masses), plt.array(distances)


def fit_data(file_name):
    masses, distances = get_data(file_name)
    forces = masses * 9.81

    # Plot measured data
    plt.plot(forces, distances, "ko", label="Measured displacements")

    # Linear fit
    slope, intercept = plt.polyfit(forces, distances, 1)
    k = 1.0 / slope
    extended_forces = plt.arange(0, 15, 0.1)
    linear_pred = slope * extended_forces + intercept

    # Plot linear fit (solid and dotted)
    plt.plot(
        extended_forces,
        linear_pred,
        color="gray",
        linewidth=3,
        label=f"Displacements predicted by\nlinear fit, k = {k:.5f}",
    )
    plt.plot(extended_forces, linear_pred, "k:", linewidth=1)

    # Cubic overfit
    cubic_coeffs = plt.polyfit(forces, distances, 3)
    cubic_pred = plt.polyval(cubic_coeffs, extended_forces)
    plt.plot(extended_forces, cubic_pred, "b", label="Cubic fit (overfit)")

    # Labels and display
    plt.title("Measured Displacement of Spring")
    plt.xlabel("|Force| (Newtons)")
    plt.ylabel("Distance (meters)")
    plt.legend(loc="lower left")
    plt.grid(True)
    plt.show()


fit_data("springData.txt")

# Re-import libraries after code execution environment reset
import numpy as np
import pylab as plt


def get_data(file_name):
    distances = []
    masses = []
    with open(file_name, "r") as f:
        next(f)  # skip header
        for line in f:
            d, m = line.strip().split()
            distances.append(float(d))
            masses.append(float(m))
    return np.array(masses), np.array(distances)


def r_squared(y, predicted):
    ss_res = np.sum((y - predicted) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1 - ss_res / ss_tot


def fit_and_evaluate(file_name):
    masses, distances = get_data(file_name)
    forces = masses * 9.81

    # Linear fit
    slope, intercept = np.polyfit(forces, distances, 1)
    predicted_linear = slope * forces + intercept
    r2_linear = r_squared(distances, predicted_linear)

    # Cubic fit
    cubic_coeffs = np.polyfit(forces, distances, 3)
    predicted_cubic = np.polyval(cubic_coeffs, forces)
    r2_cubic = r_squared(distances, predicted_cubic)

    # Plot data and both fits
    plt.plot(forces, distances, "ko", label="Measured displacements")

    extended_forces = np.arange(0, 15, 0.1)
    plt.plot(
        extended_forces,
        slope * extended_forces + intercept,
        color="gray",
        linewidth=3,
        label=f"Linear fit (R² = {r2_linear:.4f})",
    )

    extended_cubic = np.polyval(cubic_coeffs, extended_forces)
    plt.plot(
        extended_forces, extended_cubic, "b", label=f"Cubic fit (R² = {r2_cubic:.4f})"
    )

    plt.title("Measured Displacement of Spring with R²")
    plt.xlabel("|Force| (Newtons)")
    plt.ylabel("Distance (meters)")
    plt.legend(loc="lower left")
    plt.grid(True)
    plt.show()


fit_and_evaluate("springData.txt")

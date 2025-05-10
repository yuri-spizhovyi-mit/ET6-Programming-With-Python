import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd

# Load the data file
df = pd.read_csv("/mnt/data/data.csv")

# Extract necessary columns
df["DATE"] = df["DATE"].astype(str)
df["YEAR"] = df["DATE"].str.slice(0, 4).astype(int)
df["MONTH"] = df["DATE"].str.slice(4, 6).astype(int)
df["DAY"] = df["DATE"].str.slice(6, 8).astype(int)

# Filter for BOSTON only
boston = df[df["CITY"] == "BOSTON"]

# INTERVAL_1 = 1961 to 2005
years = list(range(1961, 2006))

# Problem 3: Jan 10 each year
jan10_temps = []
for year in years:
    temp = boston[
        (boston["YEAR"] == year) & (boston["MONTH"] == 1) & (boston["DAY"] == 10)
    ]["TEMP"]
    if not temp.empty:
        jan10_temps.append(temp.values[0])
    else:
        jan10_temps.append(np.nan)

# Problem 4: Yearly average
yearly_avg_temps = []
for year in years:
    temps = boston[boston["YEAR"] == year]["TEMP"]
    yearly_avg_temps.append(temps.mean())

# Remove NaNs if any
x_clean = np.array(years)[~np.isnan(jan10_temps)]
jan10_clean = np.array(jan10_temps)[~np.isnan(jan10_temps)]

# Generate polynomial models
jan10_model = np.polyfit(x_clean, jan10_clean, 1)
jan10_pred = np.polyval(jan10_model, x_clean)

yearly_model = np.polyfit(years, yearly_avg_temps, 1)
yearly_pred = np.polyval(yearly_model, years)


# Calculate R-squared
def r_squared(y, est):
    error = ((y - est) ** 2).sum()
    mean_error = error / len(y)
    return 1 - (mean_error / np.var(y))


r2_jan10 = r_squared(jan10_clean, jan10_pred)
r2_yearly = r_squared(np.array(years), yearly_pred)

# Plot both
plt.figure(figsize=(14, 6))

# Jan 10 plot
plt.subplot(1, 2, 1)
plt.plot(x_clean, jan10_clean, "bo", label="Jan 10 Temps")
plt.plot(x_clean, jan10_pred, "r-", label=f"Fit: R²={r2_jan10:.3f}")
plt.title("Temperature on Jan 10 Each Year (BOSTON)")
plt.xlabel("Year")
plt.ylabel("Temp (°C)")
plt.legend()

# Yearly average plot
plt.subplot(1, 2, 2)
plt.plot(years, yearly_avg_temps, "bo", label="Yearly Avg Temps")
plt.plot(years, yearly_pred, "r-", label=f"Fit: R²={r2_yearly:.3f}")
plt.title("Yearly Average Temperature (BOSTON)")
plt.xlabel("Year")
plt.ylabel("Temp (°C)")
plt.legend()

plt.tight_layout()
plt.show()

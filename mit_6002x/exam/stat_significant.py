# Re-import libraries and rerun the simulation after reset
import numpy as np
from scipy import stats
import pandas as pd

# Simulated high and low temperature data
high_temps = np.random.normal(loc=83.5, scale=6.5, size=30)
low_temps = np.random.normal(loc=67.2, scale=4.5, size=30)

# Two-sample t-test
t_stat, p_val = stats.ttest_ind(high_temps, low_temps, equal_var=False)


# Confidence interval calculation
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    se = stats.sem(data)
    margin = stats.t.ppf((1 + confidence) / 2.0, len(data) - 1) * se
    return mean, mean - margin, mean + margin


high_mean, high_ci_low, high_ci_high = confidence_interval(high_temps)
low_mean, low_ci_low, low_ci_high = confidence_interval(low_temps)

# Create result tables
results = pd.DataFrame(
    {
        "Group": ["High Temp", "Low Temp"],
        "Mean": [high_mean, low_mean],
        "95% CI Lower": [high_ci_low, low_ci_low],
        "95% CI Upper": [high_ci_high, low_ci_high],
    }
)

t_test_summary = pd.DataFrame({"t-statistic": [t_stat], "p-value": [p_val]})

print(results, t_test_summary)

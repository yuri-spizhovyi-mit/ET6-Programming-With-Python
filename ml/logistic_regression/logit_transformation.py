import numpy as np
import pandas as pd

# Define probabilities
probabilities = np.array([0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99])

# Compute odds
odds = probabilities / (1 - probabilities)

# Compute logit (log-odds)
logit_values = np.log(odds)

# Display in a table
df = pd.DataFrame(
    {"Probability": probabilities, "Odds": odds, "Logit (log-odds)": logit_values}
)

print(df)

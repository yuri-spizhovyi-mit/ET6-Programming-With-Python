import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, binomtest

# Data
heads = 7
tails = 3
n = heads + tails

# === FREQUENTIST ESTIMATE ===
freq_estimate = heads / n
print("Frequentist estimate of P(H):", round(freq_estimate, 2))

# Binomial test (is coin fair?)
result = binomtest(k=heads, n=n, p=0.5, alternative="two-sided")
print("Frequentist p-value for H0: P(H)=0.5:", round(result.pvalue, 4))

# === BAYESIAN ESTIMATE ===
# Prior: Beta(1,1) = uniform (no prior bias)
alpha_prior = 1
beta_prior = 1

# Posterior: Beta(1+7, 1+3)
alpha_post = alpha_prior + heads
beta_post = beta_prior + tails

# Range of probabilities
x = np.linspace(0, 1, 500)
posterior = beta.pdf(x, alpha_post, beta_post)

# Plot
plt.figure(figsize=(8, 4))
plt.plot(x, posterior, label=f"Posterior Beta({alpha_post},{beta_post})")
plt.axvline(freq_estimate, color="red", linestyle="--", label="Freq. Estimate")
plt.title("Bayesian Posterior for Coin Fairness")
plt.xlabel("Probability of Heads")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

def calc_bayes(prior_a, prob_b_given_a, prob_b):
    """
    Calculate the posterior probability using Bayes' Theorem.

    Parameters:
    prior_a (float): Prior probability of event A
    prob_b_given_a (float): Probability of event B given A is true
    prob_b (float): Total probability of event B

    Returns:
    float: Posterior probability of A given B
    """
    return (prior_a * prob_b_given_a) / prob_b


# Initial probabilities
prior_a = 1 / 3
prob_6_given_a = 1 / 5

# Total probability of rolling a 6 from one of three types (A, B, C)
# Assuming type B: 1/6, type C: 1/7
prob_6 = (1 / 5 + 1 / 6 + 1 / 7) / 3

# First update
post_a = calc_bayes(prior_a, prob_6_given_a, prob_6)
print("Probability of type A =", round(post_a, 4))

# Second update using updated prior
post_a = calc_bayes(post_a, prob_6_given_a, prob_6)
print("Probability of type A =", round(post_a, 4))

# bayes_housing_analysis.py


def calc_bayes(prior_a, prob_b_given_a, prob_b):
    """
    Computes the posterior probability P(A|B) using Bayes' Theorem.

    Parameters:
    - prior_a: P(A), prior probability of A
    - prob_b_given_a: P(B|A), likelihood of B given A
    - prob_b: P(B), total probability of B

    Returns:
    - P(A|B), the posterior probability
    """
    return (prior_a * prob_b_given_a) / prob_b


def example_1_buyer_type_given_budget():
    print("\nExample 1: Buyer Type Given High Budget")

    # Given probabilities
    P_investor = 0.3
    P_homebuyer = 0.7
    P_high_price_given_investor = 0.6
    P_high_price_given_homebuyer = 0.1

    # Total probability of someone looking at homes over $700k
    P_high_price = (
        P_investor * P_high_price_given_investor
        + P_homebuyer * P_high_price_given_homebuyer
    )

    # Bayes' Theorem: P(Investor | >$700k)
    P_investor_given_high_price = calc_bayes(
        P_investor, P_high_price_given_investor, P_high_price
    )

    print(
        f"Probability a buyer is an Investor given they look at >$700k homes: {round(P_investor_given_high_price, 4)}"
    )


def example_2_market_decline_given_crash_news():
    print("\nExample 2: Market Decline Given 'Crash' News Headline")

    # Given probabilities
    P_decline = 0.2
    P_not_decline = 0.8
    P_crash_given_decline = 0.7
    P_crash_given_not_decline = 0.05

    # Total probability of seeing the word "crash" in news
    P_crash = (
        P_decline * P_crash_given_decline + P_not_decline * P_crash_given_not_decline
    )

    # Bayes' Theorem: P(Decline | Crash)
    P_decline_given_crash = calc_bayes(P_decline, P_crash_given_decline, P_crash)

    print(
        f"Probability the market is declining given the news says 'crash': {round(P_decline_given_crash, 4)}"
    )


if __name__ == "__main__":
    print("=== Bayes' Theorem in Housing Market Context ===")
    example_1_buyer_type_given_budget()
    example_2_market_decline_given_crash_news()

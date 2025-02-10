"""
1. For each month, calculate statements on the monthly payment
2. For each month, calculate remaining balance.
3. At the end of 12 months, print out the remaining balance. Be sure to print
out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def paying_debt(
    balance: float, annualInterestRate: float, monthlyPaymentRate: float
) -> str:
    monthly_interest_rate = annualInterestRate / 12.0
    for i in range(1, 13):
        minimum_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = (
            monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        )
        # print(f"minimum_monthly_payment: {minimum_monthly_payment:.2f}")
        # print(f"monthly_unpaid_balance: {monthly_unpaid_balance:.2f}")
        print("Month " + str(i) + " Remaining balance: " + str(round(balance, 2)))
    remaining_balance = round(balance, 2)
    print("Remaining balance: " + str(remaining_balance))


paying_debt(balance, annualInterestRate, monthlyPaymentRate)

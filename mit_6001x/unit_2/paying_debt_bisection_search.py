"""
1. For each month, calculate statements on the monthly payment
2. For each month, calculate remaining balance.
3. At the end of 12 months, print out the remaining balance. Be sure to print
out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
"""

balance = 999999
annualInterestRate = 0.18


def paying_debt(balance: float, annualInterestRate: float) -> str:
    monthly_interest_rate = annualInterestRate / 12.0
    lower_bound = balance / 12
    upper_bound = balance * 1.2 / 12
    minimum_fixed_monthly_payment = (upper_bound + lower_bound) / 2
    run = True
    while run:
        temp_balance = balance
        for i in range(12):
            monthly_unpaid_balance = temp_balance - minimum_fixed_monthly_payment
            temp_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            temp_balance = round(temp_balance, 3)
        if temp_balance == 0:
            run = False
        elif temp_balance > 0:
            lower_bound = minimum_fixed_monthly_payment
            minimum_fixed_monthly_payment = (lower_bound + upper_bound) / 2
        else:
            upper_bound = minimum_fixed_monthly_payment
            minimum_fixed_monthly_payment = (lower_bound + upper_bound) / 2
    minimum_fixed_monthly_payment = round(minimum_fixed_monthly_payment, 2)
    print("Lowest Payment: " + str(minimum_fixed_monthly_payment))


paying_debt(balance, annualInterestRate)

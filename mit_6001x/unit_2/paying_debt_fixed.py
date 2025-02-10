"""
1. For each month, calculate statements on the monthly payment
2. For each month, calculate remaining balance.
3. At the end of 12 months, print out the remaining balance. Be sure to print
out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
"""

balance = 3926
annualInterestRate = 0.2


def paying_debt(balance: float, annualInterestRate: float) -> str:
    monthly_interest_rate = annualInterestRate / 12.0
    minimum_fixed_monthly_payment = 10
    run = True
    while run:
        temp_balance = balance
        for i in range(12):
            monthly_unpaid_balance = temp_balance - minimum_fixed_monthly_payment
            temp_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        if temp_balance < 0:
            run = False
        else:
            minimum_fixed_monthly_payment += 10

    print("Lowest Payment: " + str(minimum_fixed_monthly_payment))


paying_debt(balance, annualInterestRate)


def calculate_payoff_month(balance, interest_rate, minimum_payment):
    count_months = 0

    
    while balance > 0:
        interest = balance * (interest_rate / 100 / 12)
        if minimum_payment <= interest:
            return -1
        balance = balance + interest - minimum_payment
        count_months += 1
    
    return count_months

print(calculate_payoff_month(5000, 19.99, 100))

    


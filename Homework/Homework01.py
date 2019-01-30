# PROGRAMMER: Paul Gonzales
# DATE: February 7, 2019
# ASSIGNMENT: Homework 01 (Financial application: loan amortization schedule)
# ALGORITHM: 1) prompt user to input Principal, Rate, Term;
# 2) convert annual interest into monthly interest, and convert term from years to months;
# 3) caclulate monthly payment using data provided;
# 4) loop through each monthly payment cycle calculating the interest portion, and
# principal portion of the payment, decreasing the remaining balance, and printing
# to standard out these data.


def calc_month_rate(apr):
    return (apr/100)/12

def calc_month_payment(p, j, n):
    return p*(j/(1-(1+j)**(-n)))

# Start
balance = int(input("Enter Loan Ammount: "))
numberOfYears = int(input("Enter Loan Term: "))
numberOfMonths = numberOfYears * 12
rate = int(input("Enter Interest Rate: "))

monthlyInterestRate = calc_month_rate(rate)
monthlyPayment = calc_month_payment(balance, monthlyInterestRate, numberOfMonths)

# For each iteration in the loop, compute the interest and principal and update the balance.
for i in range(1, numberOfYears * 12 + 1):

    interest = monthlyInterestRate * balance

    principal = monthlyPayment - interest

    balance = balance - principal

    print("Month: ", i, "\t", "Interest: ", round(interest, 2), "\t", "Principal: ", round(principal, 2), "\t", "Remaining Balance: ", round(balance, 2))

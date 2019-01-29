# PROGRAMMER: Paul Gonzales
# DATE: February 7, 2019
# ASSIGNMENT: Homework 01 (Financial application: loan amortization schedule)
# ALGORITHM: 1) prompt user to input Principal, Rate, Term; 2) convert annual interest into monthly interest, and convert term
# from years to months; 3) caclulate monthly payment using data provided; 4) loop through each monthly payment cycle calculating
# the interest portion, and principal portion of the payment, decreasing the remaining balance, and printing to standard out
# these data.

# Start
balance = int(input("Enter Loan Ammount: ")) # The balance is initially the loan amount.
numberOfYears = int(input("Enter Loan Term: "))
rate = int(input("Enter Interest Rate: "))


# TODO: display amortization schedule for the loan

# Since the monthly payment is the same for each month, it should be computed before the loop.
monthlyPayment = principal + interest

# For each iteration in the loop, compute the interest and principal and update the balance.
for i in range(1, numberOfYears * 12 + 1):

    interest = monthlyInterestRate * balance

    principal = monthlyPayment - interest

    balance = balance - principal

    print(i, "\t\t", interest, "\t\t", principal, "\t\t", balance)

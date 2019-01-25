# PROGRAMMER: Paul Gonzales
# DATE:   February 7, 2019
# ASSIGNMENT:  Homework 01 (Financial application: loan amortization schedule)
# ALGORITHM: How the program works.  This should be structured using short,
# descriptive phrases that are indented appropriately.


# TODO: LOOK UP SOLUTION per in class discussion; answer is in book


# The monthly payment for a given loan pays the principal and the interest.
# The monthly interest is computed by multiplying the monthly interest rate and the balance (the remaining principal).
# The principal paid for the month is therefore the monthly payment minus the monthly interest.

# Note
# The balance after the last payment may not be zero. If so, the last payment
# should be the normal monthly payment plus the final balance.


# Start
balance = input("Enter Loan Ammount: ") # The balance is initially the loan amount.
numberOfYears = input("Enter Loan Term: ")
monthlyInterestRate = input("Enter Interest Rate: ")


# TODO: display amortization schedule for the loan

# Since the monthly payment is the same for each month, it should be computed before the loop.
monthlyPayment = principal + interest

# For each iteration in the loop, compute the interest and principal and update the balance.
for i in range(1, numberOfYears * 12 + 1):

    interest = monthlyInterestRate * balance

    principal = monthlyPayment - interest

    balance = balance - principal

    print(i, "\t\t", interest, "\t\t", principal, "\t\t", balance)

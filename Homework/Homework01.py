# PROGRAMMER: Paul Gonzales
# DATE:   month day, 2019
# ASSIGNMENT:  Homework 01
# ALGORITHM: How the program works.  This should be structured using short,
# descriptive phrases that are indented appropriately.

(Financial application: loan amortization schedule)
The monthly payment for a given loan pays the principal and the interest.
The monthly interest is computed by multiplying the monthly interest rate and the balance (the remaining principal).
The principal paid for the month is therefore the monthly payment minus the monthly interest.
Write a program that lets the user enter the loan amount, number of years, and interest rate, and then displays the amortization schedule for the loan.

Note

The balance after the last payment may not be zero. If so, the last payment
should be the normal monthly payment plus the final balance.



# Variables
monthlyPayment
principal
interest
monthlyinterest = monthly interest rate * balance
balance
loanammount

Hint

Write a loop to display the table. Since the monthly payment is the same
for each month, it should be computed before the loop. The balance is
initially the loan amount. For each iteration in the loop, compute the
interest and principal and update the balance. The loop may look like this:

for i in range(1, numberOfYears * 12 + 1):

    interest = monthlyInterestRate * balance

    principal = monthlyPayment - interest

    balance = balance - principal

    print(i, "\t\t", interest, "\t\t", principal, "\t\t", balance)

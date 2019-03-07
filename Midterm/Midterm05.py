# PROGRAMMER: Paul Gonzales
# DATE: March 5, 2019
# ASSIGNMENT: Homework 05
# ALGORITHM: The user inputs the number days they would like to calculate pay.
# The program then loops through each day, printing the day, and how much pay
# has been earned for the day. The salary is updated with the current days pay,
# and penny is doubled.

def main():
    days = int(input("Enter number of days:"))
    pennys = 1
    pay = 0

    for day in range(1, days + 1):
        print("Day: " + str(day) + " Todays Pay: $" + str(pennys/100))
        pay += pennys
        pennys *= 2

    print("Your total pay is: $" + str(pay/100))

    return

if __name__ == "__main__":
    main()

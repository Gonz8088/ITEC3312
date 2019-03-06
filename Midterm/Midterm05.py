# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 05
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    days = int(input("Enter days:"))
    pennys = 1
    salary = 0

    for day in range(1, days + 1):
        print("Day: " + str(day) + " Todays Pay: $" + str(pennys/100))
        salary += pennys
        pennys *= 2

    print("Your total pay is: $" + str(salary/100))

    return

if __name__ == "__main__":
    main()

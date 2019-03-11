# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: The numberOfDaysInAYear function works by checking if the year passed
# is a multiple of 4. If so then it is a leap year and it is 366 days long.

def numberOfDaysInAYear(year):
    nonleap_year = 365
    if year % 4 == 0:
        print(str(year) + ': Days: ' + str(nonleap_year + 1))
    else:
        print(str(year) + ': Days: ' + str(nonleap_year))
    return

def main():
    for y in range(2010, 2021):
        numberOfDaysInAYear(y)
    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

from math import pi

def areaCircle(radius: int) -> float:
    """areaCircle-- returns the area of circle given the radius argument"""
    return pi * pow(radius, 2)

def main():
    medium = 12
    large = 16

    two_medium = 2 * areaCircle(medium)
    one_large = areaCircle(large)
    difference = two_medium - one_large

    print("The area of two medium pizzas is: " + str(round(two_medium)) + " sq.in.")
    print("The area of one large pizza is: " + str(round(one_large)) + " sq.in.")
    print("The difference in size is: " + str(round(difference)) + " sq.in.")
    print("The difference in price is: $3")

    return

if __name__ == "__main__":
    main()

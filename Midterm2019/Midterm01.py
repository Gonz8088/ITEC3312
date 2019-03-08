# PROGRAMMER: Paul Gonzales
# DATE: March 7, 2019
# ASSIGNMENT: Midterm 01
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def cupsSugar(cookie: int) -> float:
    """cupsSugar-- returns number of cups
    needed to make the number of cookies arguments.
    The conversion factor is (1.5 cups sugar / 48 cookies)"""
    return (cookie * 1.5)/48

def cupsButter(cookie: int) -> float:
    """cupsButter-- returns number of cups
    needed to make the number of cookies arguments.
    The conversion factor is (1 cup butter / 48 cookies)"""
    return (cookie * 1)/48

def cupsFlour(cookie: int) -> float:
    """cupsSugar-- returns number of cups
    needed to make the number of cookies arguments.
    The conversion factor is (2.75 cups flour / 48 cookies)"""
    return (cookie * 2.75)/48

def main():
    cookies = int(input("How many cookies to make? "))
    sugar = cupsSugar(cookies)
    butter = cupsButter(cookies)
    flour = cupsFlour(cookies)

    print("Cups of Sugar Needed: " + str(round(sugar, 2)))
    print("Cups of Butter Needed: " + str(round(butter, 2)))
    print("Cups of Flour Needed: " + str(round(flour, 2)))

    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 3
# ALGORITHM: Sea level is initialized at 0 since it is the starting pointself.
# The constant rate the ocean rises is 3.1 mm. for each year between 2019 up to
# but not including 2040, the sea level is incremented by the constant rate
# The year is printed and the current amount the sea level has rissen to date.

def main():
    sea_level = 0
    rate = 3.1 # mm

    for year in range(2019, 2040):
        sea_level += rate
        print("Year:" + str(year))
        print("Amount Risen: " + str(format(sea_level, '.2f')) + "mm", end='\n\n')
    return

if __name__ == "__main__":
    main()

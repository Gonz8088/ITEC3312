# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    sea_level = 0
    rate = 3.1

    for year in range(2019, 2040):
        sea_level += rate
        print("Year:" + str(year))
        print("Amount Risen: " + str(format(sea_level, '.2f')) + "mm", end='\n\n')
    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import csv
def main():
    jobs = []
    with open("C:\\TestData\\Copy of Texas2015EntryLevelWages.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            jobs.append(row)

    for row in jobs:
        if row[4].lstrip('$ ').replace(',', '').isdigit() and "web" in row[3].casefold() \
        or "network" in row[3].casefold() or "database" in row[3].casefold() \
        or "computer" in row[3].casefold() or "software" in row[3].casefold():
            print(row[3], row[4])

    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import statistics

def main():
    p = ["C:\\TestData\\"]

    p.append(input("Enter a filename: "))

    path = ""

    with open(path.join(p), 'r') as infile:
        f = infile.read()

    scores = []

    for score in f.split(sep="#"):
        scores.append(int(score))

    print("There are " + str(len(scores)) + " scores")

    print("The total is " + str(sum(scores)))

    print("The avearge is " + str(statistics.mean(scores)))

    return

if __name__ == "__main__":
    main()

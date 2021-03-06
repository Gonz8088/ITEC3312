# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    with open("C://TestData//golf.txt", 'r') as infile:
        for line in infile:
            record = line.split(sep=',')
            print("Golfer: {0} \tScore: {1}".format(record[0], record[1]))
    return

if __name__ == "__main__":
    main()

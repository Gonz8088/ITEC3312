# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    numbers = []

    while True:
        x = int(input("Eneter a number (0: for end of input): "))
        if x == 0:
            numbers.append(x)
            break
        else:
            numbers.append(x)

    maax = max(numbers)
    count = numbers.count(maax)

    print("The largest number is " + str(maax))
    print("The occurence count of the largest number is " + str(count))

    return

if __name__ == "__main__":
    main()

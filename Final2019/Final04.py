# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    with open("C:\\TestData\\FWQ4first_file.txt", 'r') as file:
        file1 = file.read()

    with open("C:\\TestData\\FWQ4second_file.txt", 'r') as file:
        file2 = file.read()

    set1 = {word for word in file1.split()}
    set2 = {word for word in file2.split()}

    return

if __name__ == "__main__":
    main()

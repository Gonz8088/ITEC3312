# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

<<<<<<< HEAD
def main():
    with open("C:\\TestData\\FWQ4first_file.txt", 'r') as file:
        file1 = file.read()

    with open("C:\\TestData\\FWQ4second_file.txt", 'r') as file:
        file2 = file.read()

    set1 = {word for word in file1.split()}
    set2 = {word for word in file2.split()}
=======
import re

def main():
    with open("C:\\TestData\\FWQ4first_file.txt", 'r') as infile:
        f1 = infile.read()
        f1 = f1.lower()

    with open("C:\\TestData\\FWQ4second_file.txt", 'r') as infile:
        f2 = infile.read()
        f2 = f2.lower()

    file1, file2 = [], []

    for word in f1.split():
        file1.append(re.sub(r"[^\w\d\s]+", '', word))

    for word in f2.split():
        file2.append(re.sub(r"[^\w\d\s]+", '', word))

    file1, file2 = set(file1), set(file2)

    print("Print all words from both files: ")
    for word in file1.union(file2):
        print(word)

    print("Print words contained in both files: ")
    for word in file1.intersection(file2):
        print(word)

    print("Print words in file1 not in file2: ")
    for word in file1.difference(file2):
        print(word)

    print("Print words in file2 not in file1: ")
    for word in file2.difference(file1):
        print(word)

    print("Print words in file1 & file2 but not in both: ")
    for word in file1.symmetric_difference(file2):
        print(word)
>>>>>>> 5810a299d81b3cf6127db3c2ea98f23c75908a5b

    return

if __name__ == "__main__":
    main()

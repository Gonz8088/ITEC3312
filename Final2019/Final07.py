# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

from os import listdir, chdir, getcwd

def count_pyfiles():
    for file in listdir():
        if file.endswith('.py'):
            yield file

def main():
    print("Your current working directory is: " + getcwd())
    cd = input("Which directory do you want to search for .py files? ")
    chdir(cd)

    count = 0
    for f in count_pyfiles():
        count += 1
        print(f)
    print("--- " + str(count) + " .py files found")

    return

if __name__ == "__main__":
    main()

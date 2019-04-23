# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import os
import os.path

def main():
    for dirpath, dirnames, filenames in os.walk("c:/TestData/"):
        for filename in (f for f in filenames if len(f) > 10):
            print(os.path.join(dirpath, filename))
    return None

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import os

def readfiles(filenames):
    for ls in filenames:
        for file in ls:
            for line in open(os.path.join("C:/TestData/", file)):
                yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line)

def main():
    lines = readfiles(filenames for dirpath, dirnames, filenames in os.walk("c:/TestData/"))
    lines = grep("PG", lines)
    printlines(lines)

if __name__ == "__main__":
    main()

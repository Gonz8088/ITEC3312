# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def count(s: str, ch: str) -> int:
    i = 0
    count = 0
    while True:
        i = s.find(ch, i)
        if i == -1:
            break
        else:
            count += 1
            i += 1
    return count

def main():
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")

    print("Ther are " + str(count(string, substring)) + " occurences of " + substring + " in " + string)
    
    return

if __name__ == "__main__":
    main()

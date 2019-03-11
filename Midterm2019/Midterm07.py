# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: The count function loops thourgh starting from the first position
# in the string, and uses find the get the index of the first occurence of the
# substring. If find returns a -1 then it breaks the loop because no instance
# of substring was found. Otherwise it updates the count, and increments the index
# position by one so that find will begin search one position past the first occurence.

def count(s: str, ch: str) -> int:
    """count--
    returns the count of the number incidence
    of the ch substring in the s string"""
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

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm 09
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def checkPassword(password: str) -> bool:
    length = len(password) >= 8
    alphanumeric = password.isalnum()
    atleasttwo = None
    numbers = []

    for i in range(10):
        if i == 0:
            numbers.insert(i, password.count(str(i)))
        elif i == 1:
            numbers.insert(i, password.count(str(i)))
        elif i == 2:
            numbers.insert(i, password.count(str(i)))
        elif i == 3:
            numbers.insert(i, password.count(str(i)))
        elif i == 4:
            numbers.insert(i, password.count(str(i)))
        elif i == 5:
            numbers.insert(i, password.count(str(i)))
        elif i == 6:
            numbers.insert(i, password.count(str(i)))
        elif i == 7:
            numbers.insert(i, password.count(str(i)))
        elif i == 8:
            numbers.insert(i, password.count(str(i)))
        elif i == 9:
            numbers.insert(i, password.count(str(i)))
        else:
            pass

    if sum(numbers) >= 2:
        atleasttwo = True

    if length == True and alphanumeric == True and atleasttwo == True:
        return True
    else:
        return False

def main():
    mypassword = input("Enter Password to Check: ")

    if checkPassword(mypassword):
        print("This is a good password")
    else:
        print("This is a bad password")
    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 9
# ALGORITHM: The user is prompted to enter the number of students using try ..except
# block. If the user doesn't input an integer number, an exception is raised.
# The loop iterates for the number of students stored in num_students. A try ..except
# block is also used to check for an integer value. Each iteration of the loop
# adds a dictionary item to scores using the student name as a key, and score as
# the value. A second loop the checks each item in scores, and compares the values
# It checks if the current score is higher than highest_2nd, if it is is stores
# the item, otherwise it discards it. It then checks if the value stored in
# highest_2nd is greater than highest. If it is, it stores it and highest, and
# sets highest_2nd to is previous item, otherwise it nothing is stored in highest.
# The highest and 2nd highest scores are displayed.

def main():
    while True:
        try:
            num_students = int(input("Enter The Number of Students: "))
            break
        except ValueError:
            print("Invalid input.  Try again...")

    scores = {}
    for stu in range(num_students):
        name = input("Enter Student Name: ")
        while True:
            try:
                score = int(input("Enter Student Score: "))
                break
            except ValueError:
                print("Invalid input.  Try again...")
        scores[name] = score

    highest = (None, 0)
    highest_2nd = (None, 0)
    for scr in scores.items():
        if scr[1] > highest_2nd[1]:
            previous = highest_2nd
            highest_2nd = scr
            if highest_2nd[1] > highest[1]:
                highest = highest_2nd
                highest_2nd = previous

    print(f"The highest score is: {highest[0]}: {highest[1]}")
    print(f"The 2nd highest score is: {highest_2nd[0]}: {highest_2nd[1]}")

    return

if __name__ == "__main__":
    main()

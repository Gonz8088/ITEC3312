# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

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

    return None

if __name__ == "__main__":
    main()

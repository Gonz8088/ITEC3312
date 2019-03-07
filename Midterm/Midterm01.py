# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 01
# ALGORITHM: The while loop uses the x as a counter starting at 2. It prints
# 1/x each iteration and increments by 1self.
# The for loop uses an iterator starting from 2 and ending before 11. It prints
# 1/x each iteration.

def main():
    x = 2
    # loop 1
    while x < 11:
        print(1/x)
        x +=1

    # loop 2
    for x in range(2, 11):
        print(1/x)

    return

if __name__ == "__main__":
    main()

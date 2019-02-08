# PROGRAMMER: Paul Gonzales
# DATE:   February 14, 2019
# ASSIGNMENT:  Homework 02
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

# Craps is a popular dice game played in casinos. Write a program to play a variation of the game, as follows:
# 1) Roll two dice. Each die has six faces representing values 1, 2, ..., and 6, respectively.
# 2) Check the sum of the two dice.
#     if the sum is 2, 3, or 12 (called craps), you lose;
#     if the sum is 7 or 11 (called natural), you win;
#     if the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established.
# 3) Continue to roll the dice until either a 7 or the same point value is rolled.
#     if 7 is rolled, you lose.
#     Otherwise, you win.
# Remember to incorporate functions into your code.

import random

def check_win(d1, d2):
    if d1 + d2 == 7 or d1 + d2 == 11:
        print("You win.")
        return 1
    else:
        return 0

def check_lose(d1, d2):
    if d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
        print("You lost.")
        return 1
    else:
        return 0

def main():
    point = 0
    
    while True or point != 7:
        die_1 = random.randrange(1, 7)
        die_2 = random.randrange(1, 7)
        print("You rolled a", die_1, ", and a", die_2)
        if check_win(die_1, die_2) == True:
            break
        elif check_lose(die_1, die_2) == True:
            break
        else:
            point +=1
    return

if __name__ == "__main__":
    main()

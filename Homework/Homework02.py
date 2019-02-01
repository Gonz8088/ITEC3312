# PROGRAMMER: Paul Gonzales
# DATE:   February 7, 2019
# ASSIGNMENT:  Homework #00
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

def check_win():
    # TODO:
    return
def check_lose():
    # TODO:
    return

die_1 = random(1, 6)
die_2 = random(1, 6)
point = 0

if die_1 + die_2 == 2 or die_1 + die_2 == 3 or die_1 + die_2 == 12:
    print("You lost.")
elif die_1 + die_2 == 7 or die_1 + die_2 == 11:
    print("You win.")
else:
    point +=1

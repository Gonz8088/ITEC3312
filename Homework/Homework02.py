# PROGRAMMER: Paul Gonzales
# DATE: February 14, 2019
# ASSIGNMENT: Homework 02
# ALGORITHM: The randrange function returns a value between 1, and 6 to each die.
# The while loop is continuous until a break is reached within one of the function calls.
# The logic determines if it is the first roll or not. If it is, then check_game is called first.
# If the game hasn't been won, or lost, then a point is established, and the loop iterates again .
# After the first roll, the game then checks the point for either a win or loss, and continues until one of these
# is encountered

import random

def check_point(d1, d2, p):
    if d1 + d2 == p:
        print("You win.")
        return 1
    elif d1 + d2 == 7:
        print("You lost.")
        return 1
    else:
        pass

def check_game(d1, d2):
    if d1 + d2 == 7 or d1 + d2 == 11:
        print("You win.")
        return 1
    elif d1 + d2 == 2 or d1 + d2 == 3 or d1 + d2 == 12:
        print("You lost.")
        return 1
    else:
        p = d1 + d2
        print("The point is: " + str(p))
        return p

def main():
    point = 0
    roll_count = 1
    win = False
    die_1 = random.randrange(1, 7)
    die_2 = random.randrange(1, 7)

    while True:
        print("Roll Count: " + str(roll_count) + " You rolled a " + str(die_1) \
         + ", and a " + str(die_2))

        if roll_count > 1:
            if check_point(die_1, die_2, point) == 1:
                break
        else:
            if check_game(die_1, die_2) == 1:
                break
            else:
                point = check_game(die_1, die_2)

        roll_count +=1
        die_1 = random.randrange(1, 7)
        die_2 = random.randrange(1, 7)

    return

if __name__ == "__main__":
    main()

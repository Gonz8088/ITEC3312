# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import random

class bot:
    # attributes
    self.__turn

    # methods
    def getTurn():
        return self.__turn

class human:
    # attributes
    self.__name
    self.__turn
    self.__choice

    # methods
    def setName():
        name = input("Enter Name: ")
        self.__name = name

    def getName():
        return self.__name

    def setTurn():
        turn = input("Enter Choice: ")
        self.__turn = turn

    def getTurn():
        return self.__turn

    def wantToPlayaGame():
        choice = input("Do you want to play a game?")
        self.__choice = choice
        return choice

class game:
    outcomes = ("rock", "paper", "scissors")
    # attributes
    self.__gameActive
    self.__humanPlayer = human()
    self.__botPlayer = bot()

    # methods
    def playGame():
        self.__humanPlayer.setName()
        self.__humanPlayer.setTurn()

    def get_gameActivity():
        return self.__gameActive

    def set_gameActivity():

def main():
    mygame = game()
    mygame.playGame()
    return None

if __name__ == "__main__":
    main()

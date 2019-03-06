# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 10
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import random

class bot:
    name = "bot"
    # attributes
    def __init__(self):
        self.__turn = 0

    # methods
    def setTurn(self):
        self.__turn = random.randint(1, 3)

    def getTurn(self):
        return self.__turn

class human:
    # attributes
    def __init__(self):
        self.__name = ""
        self.__turn = 0

    # methods
    def setName(self, player: str):
        self.__name = player

    def getName(self) -> str:
        return self.__name

    def setTurn(self, choice: int):
        self.__turn = choice

    def getTurn(self) -> int:
        return self.__turn

class game:
    outcomes = ("rock", "paper", "scissors")
    title = f"""\tROCK PAPER SCISSORS \n===================================\n"""
    controls = f"Moves: 1) {outcomes[0]}, 2) {outcomes[1]}, or 3) {outcomes[2]}"

    # attributes
    def __init__(self):
        self.__humanPlayer = human()
        self.__botPlayer = bot()

    # methods
    def whatMove(self, choice: int) -> str:
        if choice == 1:
            return "rock"
        elif choice == 2:
            return "paper"
        elif choice == 3:
            return "scissors"
        else:
            return "something went wrong"

    def checkWinner(self, human: int, bot: int) -> str:
        winner = [['draw', 'bot', 'human'], ['human', 'draw', 'bot'], ['bot', 'human', 'draw']]
        return winner[human-1][bot-1]

    def playGame(self):
        print(self.title)
        print(self.controls)
        playername = input("Please Enter Name: ")
        self.__humanPlayer.setName(playername)
        print("Hello " + self.__humanPlayer.getName())
        self.__botPlayer.setTurn()
        turn = int(input("Enter Choice: "))
        self.__humanPlayer.setTurn(turn)
        print(self.__humanPlayer.getName() + " played: " + self.whatMove(self.__humanPlayer.getTurn()))
        print("Bot played: " + self.whatMove(self.__botPlayer.getTurn()))
        print("The winner is: " + self.checkWinner(self.__humanPlayer.getTurn(), self.__botPlayer.getTurn()))

def main():
    choice = ""
    while True:
        mygame = game()
        mygame.playGame()
        print("Would you like to play again?")
        playagain = input("Any key to continue... (Q) to quit")
        if playagain == "Q" or playagain == "q":
            break

    return

if __name__ == "__main__":
    main()

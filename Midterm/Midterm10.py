# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 10
# ALGORITHM: Three classes are used: one for the bot, one for the player, and
# one for the game that is being played. When a game object is created, it creates
# a bot, and human object for the current game. The bot and human objects have
# getter and setter functions for the turn values, and the name of the human.
# The game displays game info for each game, and then gets the user name, and turn
# The game then checks the human turn, and bot turn and compares them to possible
# events in the game stored in winner line 68. The winner is returned in the
# checkWinner function.

import random

class bot:
    name = "bot"
    # attributes
    def __init__(self):
        self.__turn = 0

    # methods
    def setTurn(self):
        self.__turn = random.randint(1, 3)

    def getTurn(self) -> int:
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
            return self.outcomes[0]
        elif choice == 2:
            return self.outcomes[1]
        elif choice == 3:
            return self.outcomes[2]
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

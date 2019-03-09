# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm 08
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

class Stock():
    def __init__(self):
        self.__symbol = ""
        self.__name = ""
        self.__previousClosingPrice = 0.0
        self.__currentPrice = 0.0

    def getStockName(self) -> str:
        return self.__name

    def getStockSymbol(self) -> str:
        return self.__symbol

    def getPreviousPrice(self) -> float:
        return self.__previousClosingPrice

    def getCurrentPrice(self) -> float:
        return self.__currentPrice

    def getChangePercent(self) -> float:
        return # percent change


def main():
    return

if __name__ == "__main__":
    main()

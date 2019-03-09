# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm 08
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

class Stock():
    def __init__(self, name: str, symbol: str, prev_price: float, cur_price: float):
        self.__name = name
        self.__symbol = symbol
        self.__previousClosingPrice = prev_price
        self.__currentPrice = cur_price

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

    def


def main():
    return

if __name__ == "__main__":
    main()

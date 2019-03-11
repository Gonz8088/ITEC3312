# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm 08
# ALGORITHM: An instance of the Stock class is created, with name, symbol
# previous price, and current price passed to it. The getChangePercent method is
# invoked and returns the quotient of current price over previous price.

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
        return self.__currentPrice/self.__previousClosingPrice

    def setPreviousPrice(self, price: float):
        self.__previousClosingPrice = price

    def setCurrentPrice(self, price: float):
        self.__currentPrice = price


def main():
    mystock = Stock("Intel Corporation", "INTC", 20.5, 20.35)
    print("The Price Change: " + str(round(mystock.getChangePercent(), 1)) + '%')

    return

if __name__ == "__main__":
    main()

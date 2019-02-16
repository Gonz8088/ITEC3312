# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 04
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

from datetime import datetime as dt

class StopWatch:
    """docstring for StopWatch."""
    def __init__(self):
        self.__startTime = dt.time().now()
        self.__endTime = None

    def get_startTime(self):
        return self.__startTime

    def get_endTime(self):
        return self.__endTime

    def get_ElapsedTime(self):
        return self.__endTime - self.__startTime

    def start(self):
        self.__startTime = dt.time().now()
        return

    def stop(self):
        self.__endTime = dt.time().now()
        return


def main():
    stopwatch = StopWatch()
    for i in range(1000000):
        i += i
    stopwatch.get_ElapsedTime()

    return

if __name__ == "__main__":
    main()

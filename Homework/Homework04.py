# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 04
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

from datetime import datetime as dt
from datetime import timedelta as td

class StopWatch:
    """docstring for StopWatch."""
    def __init__(self):
        self.__startTime = dt.now().time()
        self.__endTime = None

    def get_startTime(self):
        return self.__startTime

    def get_endTime(self):
        return self.__endTime

    def get_ElapsedTime(self):
        __c = td(hours=__startTime.hour, minutes=__startTime.minute, \
        seconds=__startTime.second, milliseconds=__startTime.millisecond)
        __d = td(hours=__endTime.hour, minutes=__endTime.minute, \
        seconds=__endTime.second, milliseconds=__endTime.millisecond)
        return str(d-c)

    def start(self):
        self.__startTime = dt.now().time()
        return

    def stop(self):
        self.__endTime = dt.now().time()
        return


def main():
    stopwatch = StopWatch()
    for i in range(1000000):
        i += i
    stopwatch.get_ElapsedTime()

    return

if __name__ == "__main__":
    main()

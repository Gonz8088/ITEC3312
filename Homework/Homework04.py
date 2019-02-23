# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 04
# ALGORITHM: The StopWatch class is built according to the specification,
# and uses a datetime object, and timedelta object from the datetime moduleself.
# when a StopWatch object is created, the __startTime attribute is initialized
# using the now().time() method. The for loop adds the sum of integers from 1 to
# 1000000, and then the stopwatch.stop() method is called to get the current time
# at the end of the loop. The elapsed time is then determined by creating timedelta
# objects. One for the __startTime, and one for the __endTime. The __startTime
# timedelta object is subtracted from the __endTime timedelta object, and the
# result is returned as a string.

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
        self.__c = td(hours=self.__startTime.hour, minutes=self.__startTime.minute, \
        seconds=self.__startTime.second, milliseconds=self.__startTime.microsecond)
        self.__d = td(hours=self.__endTime.hour, minutes=self.__endTime.minute, \
        seconds=self.__endTime.second, milliseconds=self.__endTime.microsecond)
        return str(self.__d-self.__c)

    def start(self):
        self.__startTime = dt.now().time()
        return

    def stop(self):
        self.__endTime = dt.now().time()
        return


def main():
    stopwatch = StopWatch()

    for i in range(1000001):
        i += i

    stopwatch.stop()
    print("Sum:", i)
    print("Elapsed Time:", stopwatch.get_ElapsedTime())

    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

from datetime import datetime, timedelta

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, startTime, elapseTime):
        newTime = startTime + elapseTime
        self.__hour = newTime.hour
        self.__minute = newTime.minute
        self.__second = newTime.second
        return

    def getTime(self):
        hr = str(self.__hour)
        min = str(self.__minute)
        sec = str(self.__second)
        return f"{hr}:{min}:{sec}"

def main():
    t = datetime.now()
    time = Time(t.hour, t.minute, t.second)
    print("Current time is {0}:{1}:{2}".format(str(t.hour), str(t.minute), str(t.second)))
    s = int(input("Enter the elapsed time: "))
    td = timedelta(seconds=s)
    time.setTime(t, td)
    print("The hour:minute:second for the elapsed time is ", time.getTime())

    return

if __name__ == "__main__":
    main()

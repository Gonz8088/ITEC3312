# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import re

def main():
    #The format needed is YYYY-MM-DD
    mdyRegex = r"([0-1]{0,1})([0-9])(/)([0-3]*)([0-9])(/)(\d{2,4})"
    dmyRegex = r"([0-3]{0,1})([0-9])(/)([0-1]*)([0-9])(/)(\d{2,4})"
    ymdRegex = r"(\d{2,4})(/)([0-1]*)([0-9])(/)([0-3]*)([0-9])"

    formatmdy = r"\7-\1\2-\4\5"
    formatdmy = r"\7-\4\5-\1\2"
    formatymd = r"\1-\3\4-\6\7"

    date = input("Enter a date in a format of DD/MM/YYYY or MM/DD/YYYY or YYYY/MM/DD: ")
    match = re.match(mdyRegex, date)
    if match:
        date = re.sub(mdyRegex, formatmdy, date)
        print(date, '1')
        exit()

    match = re.match(dmyRegex, date)
    if match:
        date = re.sub(dmyRegex, formatdmy, date)
        print(date, '2')
        exit()

    match = re.match(ymdRegex, date)
    if match:
        date = re.sub(ymdRegex, formatymd, date)
        print(date, '3')
        exit()

    return

if __name__ == "__main__":
    main()

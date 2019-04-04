# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 05
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.



#Download the TXBabyNames.txt file from Blackboard and put it into your TestData folder. Look at it, then write code to read it into a list.

#Next, answer the following questions:

#1.  How many girl babies have been born since 1910?

#2.  How many boy babies have been born since 1910?

#3.  How many girl babies were born 1910?  In 2012?

#4.  How many boy babies were born in 1910?  In 2012?

#5.  What are the total number of babies born in Texas in 2012?

#6.  What are the total number of babies born in Texas with your name since 1910? #If you have an uncommon name, look for the first name of our new UHCL president - Ira.

#7.  What are the total number of babies born in Texas with your name between 1910 and 1960? #If you have an uncommon name, look for the first name of our new UHCL president - Ira.

8.  What name was the most popular (had the highest count in one year): List the count for boys and then for girls.

9.  What name was that? List the name that was the most popular for boys  and then for girls.

10.  What year was that? List the year the name was the most popular for boys and then for girls.

11.  In what year was your name (or Ira's name) the most popular (had the highest count)?

# Write all this information out to a file.

def main():
    with open("TXBabyNames.txt", 'r') as names:
        txnames = names.readlines()

    boys = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'M':
            boys += int(record[2])

    girls = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'F':
            girls += int(record[2])

    boys1910 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'M' and "1910" in record[0]:
            boys1910 += int(record[2])
    boys2012 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'M' and "2012" in record[0]:
            boys2012 += int(record[2])

    girls1910 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'F' and "1910" in record[0]:
            girls1910 += int(record[2])

    girls2012 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if record[0][3] == 'F' and "2012" in record[0]:
            girls2012 += int(record[2])

    babys2012 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if "2012" in record[0]:
            babys2012 += int(record[2])

    paul1910 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if int(record[5:9]) >= 1910 and record[0][10:14] == "Paul":
            paul1910 += int(record[2])

    paul10thru60 = 0
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if int(record[0][5:9]) >= 1910 and int(record[0][5:9]) <= 1960 and record[0][10:14] == "Paul":
            paul10thru60 += int(record[2])

    highestboy = ("", 0)
    for i in range(len(txnames)):
        record = txnames[i].strip().rpartition(',')
        if int(record[2]) > highestboy[1]:
            highestboy = # finish here

    return

if __name__ == "__main__":
    main()

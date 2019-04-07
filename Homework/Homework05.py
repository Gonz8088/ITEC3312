# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 05
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

#8.  What name was the most popular (had the highest count in one year): List the count for boys and then for girls.

9.  What name was that? List the name that was the most popular for boys  and then for girls.

10.  What year was that? List the year the name was the most popular for boys and then for girls.

11.  In what year was your name (or Ira's name) the most popular (had the highest count)?

# Write all this information out to a file.

def gender_count(gender):
    total = 0
    for name in txnames:
        record = name.strip().rpartition(',')
        if record[0][3] == gender:
            total += int(record[2])
    return total

def gender_count_by_year(gender, year):
    total = 0
    for name in txnames:
        record = name.strip().rpartition(',')
        if record[0][3] == gender and int(record[0][5:9]) == year:
            total += int(record[2])
    return total

def count_by_year(year):
    total = 0
    for name in txnames:
        record = name[i].strip().rpartition(',')
        if int(record[0][5:9]) == year:
            total += int(record[2])
    return total

def count_by_name(name):
    total = 0
    for name in txnames:
        record = name[i].strip().rpartition(',')
        if record[0][10:14] == "Paul":
            total += int(record[2])
    return total

def name_count_by_range(name, a_year, b_year):
    total = 0
    for name in txnames:
        record = name[i].strip().rpartition(',')
        if record[0][10:14] == "Paul" and int(record[0][5:9]) >= a_year and int(record[0][5:9]) <= b_year:
            total += int(record[2])
    return total

def most_popular_by_gender(gender):
    most_pop = ("", ',', 0)
    for name in txnames:
        record = name.strip().rpartition(',')
        if record[0][3] == gender and int(record[2]) > int(most_pop[2]):
            most_pop = record
    return most_pop

def year_name_most_pop(name):
    highest = ("", ',', 0)
    for name in txnames:
        record = name.strip().rpartition(',')
        if record[0][10:14] == name and int(record[2]) > int(highest[2]):
            highest = record
    return highest

def main():
    with open("TXBabyNames.txt", 'r') as names:
        txnames = names.readlines()

    total_boys = gender_count('M')
    total_girls = gender_count('F')
    tot_boys_1910 = gender_count_by_year('M', 1910)
    tot_boys_2012 = gender_count_by_year('M', 2012)
    tot_girls_1910 = gender_count_by_year('F', 2010)
    tot_girls_2012 = gender_count_by_year('F', 2012)
    tot_babys_2012 = count_by_year(2012)
    tot_paul = count_by_name("Paul")
    tot_paul_10_thru_60 = name_count_by_range("Paul", 1910, 1960)
    popular_boy = most_popular_by_gender('M')
    popular_girl = most_popular_by_gender('F')
    year_paul_most_pop = year_name_most_pop("Paul")

    return

if __name__ == "__main__":
    main()

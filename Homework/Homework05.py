# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 05
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def gender_count(gender, names):
    total = 0
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][3] == gender:
            total += int(record[2])
    return total

def gender_count_by_year(gender, year, names):
    total = 0
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][3] == gender and int(record[0][5:9]) == year:
            total += int(record[2])
    return total

def count_by_year(year, names):
    total = 0
    for name in names:
        record = name.strip().rpartition(',')
        if int(record[0][5:9]) == year:
            total += int(record[2])
    return total

def count_by_name(name, names):
    total = 0
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][10:14] == "Paul":
            total += int(record[2])
    return total

def name_count_by_range(name, a_year, b_year, names):
    total = 0
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][10:14] == "Paul" and int(record[0][5:9]) >= a_year and int(record[0][5:9]) <= b_year:
            total += int(record[2])
    return total

def most_popular_by_gender(gender, names):
    most_pop = ("", ',', 0)
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][3] == gender and int(record[2]) > int(most_pop[2]):
            most_pop = record
    return most_pop

def year_name_most_pop(name_, names):
    highest = ("", ',', '0')
    for name in names:
        record = name.strip().rpartition(',')
        if record[0][10:] == name_ and int(record[2]) > int(highest[2]):
            highest = record
    return highest

def main():
    with open("TXBabyNames.txt", 'r') as names:
        txnames = names.readlines()

    total_boys = gender_count('M', txnames)
    total_girls = gender_count('F', txnames)
    tot_boys_1910 = gender_count_by_year('M', 1910, txnames)
    tot_boys_2012 = gender_count_by_year('M', 2012, txnames)
    tot_girls_1910 = gender_count_by_year('F', 2010, txnames)
    tot_girls_2012 = gender_count_by_year('F', 2012, txnames)
    tot_babys_2012 = count_by_year(2012, txnames)
    tot_paul = count_by_name("Paul", txnames)
    tot_paul_10_thru_60 = name_count_by_range("Paul", 1910, 1960, txnames)
    popular_boy = most_popular_by_gender('M', txnames)
    popular_girl = most_popular_by_gender('F', txnames)
    year_paul_most_pop = year_name_most_pop("Paul", txnames)

    with open("OutData.txt", 'w') as outfile:
        outfile.write("The number of girl babies born since 1910: " + str(total_girls) + '\n')
        outfile.write("The number of boy babies born since 1910: " + str(total_boys) + '\n')
        outfile.write("The number of girl babies born in 1910: " + str(tot_girls_1910) + '\n')
        outfile.write("The number of boy babies born in 1910: " + str(tot_boys_1910) + '\n')
        outfile.write("The number of girl babies born in 2012: " + str(tot_girls_2012) + '\n')
        outfile.write("The number of boy babies born in 2012: " + str(tot_boys_2012) + '\n')
        outfile.write("The number of babies born in 2012: " + str(tot_babys_2012) + '\n')
        outfile.write("The number of babies named Paul born since 1910: " + str(tot_paul) + '\n')
        outfile.write("The number of babies named Paul born between 1910 and 1960: " + str(tot_paul_10_thru_60) + '\n')
        outfile.write("The most popular name for boys: " + popular_boy[0][10:] + " in " + popular_boy[0][5:9] + '\n')
        outfile.write("The most popular name for girls: " + popular_girl[0][10:] + " in " + popular_girl[0][5:9] + '\n')
        outfile.write("The name Paul was most popular in: " + year_paul_most_pop[0][5:9] + '\n')

    return

if __name__ == "__main__":
    main()

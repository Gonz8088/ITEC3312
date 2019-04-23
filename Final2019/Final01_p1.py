# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():

    playerscores = {}
    while True:
        name = input("Enter your name: ")
        playerscores[name] = input("Enter your score: ")
        cont = input("Press m key to enter another record: ")
        if cont != 'm':
            break

    with open("C://TestData//golf.txt", 'w') as outfile:
        for k, v in playerscores.items():
            outfile.write(k + ',' + v + '\n')

    return

if __name__ == "__main__":
    main()

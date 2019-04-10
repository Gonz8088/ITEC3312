# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    with open("CROSSWD.txt", 'r') as file:
        word_list = file.readlines()

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, \
    "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, \
    "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

    scrabble_rack = input("Enter the letters in your Scrablle rack: ")

    for word in word_list:
        for letter in word.strip():
            if letter in scrabble_rack:
                pass
            else:
                break
        else:
            print(word)

    return

if __name__ == "__main__":
    main()


# lets try using str.count(sub[,start][,end])

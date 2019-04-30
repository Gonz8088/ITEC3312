# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import re

def main():
    with open("C:\\TestData\\HarryPotterAndTheSorcerersStone.txt", 'r') as infile:
        text = infile.read()

    text = text.lower()
    words = []
    for line in text:
        for word in line.split():
            words.append(re.sub(r"[^\w\d\s]+", '', word))

    word_keys = set(words)
    word_keys = sorted(word_keys)
    word_freqs = {}
    for word in word_keys:
        word_freqs[word] = words.count(word)

    for k, v in word_freqs.items():
        print(k, " occurs ", v, " times.")

    return

if __name__ == "__main__":
    main()

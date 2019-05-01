# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

import re, collections

def main():
    with open("C:\\TestData\\HarryPotterAndTheSorcerersStone.txt", 'r') as infile:
        text = infile.readlines()

    sentences = []
    for line in text:
        sentences.append(line.lower().strip())

    words = []
    for sentence in sentences:
        for word in sentence.split():
            words.append(re.sub(r"[^\w\d\s]+", '', word))
    words = sorted(words)

    word_freqs = collections.Counter(words)
    for k, v in word_freqs.items():
        print(k, "\toccurs\t", v, "\ttimes.")

    return

if __name__ == "__main__":
    main()

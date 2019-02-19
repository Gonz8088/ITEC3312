# PROGRAMMER: Paul Gonzales
# DATE: February 21, 2019
# ASSIGNMENT: Homework 03
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def getNumber(uppercaseLetter):
    keypad = {
    2: 'ABCabc',
    3: 'DEFdef',
    4: 'GHIghi',
    5: 'JKLjkl',
    6: 'MNOmno',
    7: 'PQRSpqrs',
    8: 'TUVtuv',
    9: 'WXYZwxyz'
    }

    for kv_pair in iter(keypad.items()):
        if uppercaseLetter in kv_pair[1]:
            return kv_pair[0]
        else:
            pass

def main():
    phone_number = input("Enter a string:").replace('-', '')
    if phone_number.isnumeric():
        print(format(int(phone_number[:-1]), ',').replace(',', '-') + phone_number[-1])
    else:
        for char in phone_number:
            if char.isalpha():
                phone_number = phone_number.replace(char, str(getNumber(char)))
        print(format(int(phone_number[:-1]), ',').replace(',', '-') + phone_number[-1])

    return None

if __name__ == "__main__":
    main()

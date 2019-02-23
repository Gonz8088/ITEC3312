# PROGRAMMER: Paul Gonzales
# DATE: February 21, 2019
# ASSIGNMENT: Homework 03
# ALGORITHM: The getNumber function takes a single character as input and
# checks each key/value pair in keypad and compares the character to each
# string value. When it finds a match, it will return its key (an integer).
# The user enters a phone number. If the phone number is all numeric values
# The number is printed as is. Otherwise each character of the string is checked
# to see if it is a letter and if it is, the digit is retrieved using the getNumber
# function, and replaced with its corresponding digit.

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

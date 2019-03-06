# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def main():
    unitprice = 229.00
    discount = 0.0
    print("How Many Software Modules Would You Like to order?")
    quantity = int(input("Enter Order Amount:"))

    if 10 <= quantity <= 19:
        discount = 0.10
    elif 20 <= quantity <= 29:
        discount = 0.15
    elif 30 <= quantity <= 49:
        discount = 0.25
    elif 50 <= quantity:
        discount = 0.30

    sub_total = (unitprice * quantity)
    total = sub_total - (sub_total * discount)

    print("You ordered: " + str(quantity) + " modules")
    print("Your discount is: " + str(discount * 100) + "%")
    print("Your total is: $" + str(total))
    return

if __name__ == "__main__":
    main()

# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Midterm 08
# ALGORITHM: The user is prompted to pick one of the primary colors. If the color
# is a primary, then the user is asked to pick one of the other two primary colors
# If the user doesn't pick a primary color the first time, or picks the same color1
# they will be prompted to pick again. The if ..elif structure then determines
# the combination of the two colors, and outputs the corresponding secondary color

def main():
    primaries = ("red", "blue", "yellow")
    print(f"Please choose {primaries[0]}, {primaries[1]}, or {primaries[2]}")

    while True:
        color1 = input("Please Pick a Color: ")
        if color1 in primaries:
            break
        else:
            print('\n')
            print(f"Please choose {primaries[0]}, {primaries[1]}, or {primaries[2]}")
            print("=" * 30, end='\n')

    while True:
        color2 = input("Please Pick another Color: ")
        if color2 != color1 and color2 in primaries:
            break
        elif color1 == primaries[0]:
            print('\n')
            print(f"Please choose {primaries[1]}, or {primaries[2]}")
            print("=" * 30, end='\n')
        elif color1 == primaries[1]:
            print('\n')
            print(f"Please choose {primaries[0]}, or {primaries[2]}")
            print("=" * 30, end='\n')
        else:
            print('\n')
            print(f"Please choose {primaries[0]}, or {primaries[1]}")
            print("=" * 30, end='\n')

    if (color1 == primaries[0] or color2 == primaries[0]) and (color1 == primaries[1] or color2 == primaries[1]):
        print("The secondary color is purple.")
    elif (color1 == primaries[0] or color2 == primaries[0]) and (color1 == primaries[2] or color2 == primaries[2]):
        print("The secondary color is orange.")
    elif (color1 == primaries[1] or color2 == primaries[1]) and (color1 == primaries[2] or color2 == primaries[2]):
        print("The secondary color is green.")

    return

if __name__ == "__main__":
    main()

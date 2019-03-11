# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Midterm #00
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

def oldMacDonald(pet: str) -> str:
    """oldMacDonald-- returns the sound of the given pet argument"""
    if pet == "cow":
        return "moo"
    elif pet == "pig":
        return "oink"
    elif pet == "cat":
        return "meow"
    elif pet == "duck":
        return "quack"
    elif pet == "dog":
        return "woof"

def main():
    animals = ["cow", "pig", "cat", "duck", "dog"]
    for animal in animals:
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n" \
        "And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n" \
        "With a " + oldMacDonald(animal) + ', ' + oldMacDonald(animal) + " here" \
        " and a " + oldMacDonald(animal) + ', ' + oldMacDonald(animal) + " there.\n" \
        "Here a " + oldMacDonald(animal) + ', there a ' + oldMacDonald(animal) \
        + ", everywhere a " + oldMacDonald(animal) + ', ' + oldMacDonald(animal) \
        + ".\n Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n\n")
    return

if __name__ == "__main__":
    main()

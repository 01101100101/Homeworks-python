from planet import Planet
from animals import dump_species, species

planet = Planet()
print(dump_species())


def changes(operation):
    if operation == 1:
        species_name = input("What is species name? ")
        if species_name not in species.keys():
            print("You dont have that species")
            return
        name = input("What is creature name? ")
        if name in planet.creatures:
            print("You already have creature with this name")
            return
        sex = input("What is sex?(male or female) ")
        if sex not in ["male", "female"]:
            print("we have only male or female")
            return
        planet.add_creature(name, species_name, sex)
        return
    if operation == 2:
        try:
            gr = int(input("how much food u wonna add? "))
            print(gr)
        except ValueError:
            print('it is not a number')
            return
        if gr < 0:
            print("your number is not good")
            return
        else:
            planet.grass.add(gr)
        return
    if operation == 3:
        planet.time_go()
        return
    if operation == 4:
        name = input("What is creature name? ")
        planet.show_creature(name)
        return
    if operation == 5:
        father_name = input("What is father name? ")
        mather_name = input("What is mather name? ")
        planet.give_live(father_name, mather_name)


while True:
    try:
        n = int(input("\n"
                      "1: add creature\n"
                      "2: add food\n"
                      "3: add time tick\n"
                      "4: show creature\n"
                      "5: give birth\n"
                      "6: break\n"))
    except ValueError:
        print('it is not a number')
        continue
    if not 1 <= n <= 6:
        print("your number is not good")
        continue
    if n == 6:
        break

    changes(n)

from Pet import *
import time
from Colors import *
from pathlib import Path
import json
from random import randint

pet = Pet("", "", 0, 0, 0, 0, 0, 0)

slot = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0,
    "time_hatch": 0,
}

path1 = Path("./SLOT1.json")
if path1.stat().st_size == 0:  # True if empty

    with open('SLOT1.json', 'w') as slot1:
        slot1.write("")

else:
    pass

path2 = Path("./SLOT2.json")
if path2.stat().st_size == 0:  # True if empty

    with open('SLOT2.json', 'w') as slot2:
        slot2.write("")

else:
    pass

path3 = Path("./SLOT3.json")
if path3.stat().st_size == 0:  # True if empty

    with open('SLOT3.json', 'w') as slot3:
        slot3.write("")

else:
    pass

path4 = Path("./SLOT4.json")
if path4.stat().st_size == 0:  # True if empty

    with open('SLOT4.json', 'w') as slot4:
        slot4.write("")

else:
    pass

path5 = Path("./SLOT5.json")
if path5.stat().st_size == 0:  # True if empty

    with open('SLOT5.json', 'w') as slot5:
        slot5.write("")

else:
    pass

path6 = Path("./SLOT6.json")
if path6.stat().st_size == 0:  # True if empty

    with open('SLOT6.json', 'w') as slot6:
        slot6.write("")

else:
    pass


class Aux:

    def __init__(self, p):
        self.pet = p

    @staticmethod
    def print_hatch(time_hatch):
        print(Colors.Bold + Colors.Green + "Your egg will hatch in {} seconds!".format(time_hatch) + Colors.ResetAll)
        for i in range(time_hatch):
            print("\n")
            print(
                Colors.Bold + Colors.Green + "Your egg is hatching! {} seconds left!.....".format(time_hatch - i) +
                Colors.ResetAll)
            time.sleep(1)

    @staticmethod
    def hatch():
        global pet
        time_hatch = randint(5, 10)
        print(
            Colors.Bold + Colors.Underlined + Colors.Yellow + "----- ANIMALS -----" + Colors.ResetAll)
        print("""
        Horse (EASY MODE) 🐴
        Eagle (MEDIUM MODE) 🦅
        Panther (HARD MODE) 🐯
            """)

        animal = randint(1, 3)

        if animal == 1:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your horse has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your horse's name: " + Colors.ResetAll)
            typ = "Horse"

            health = randint(75, 100)
            hunger = randint(0, 25)
            fun = randint(75, 100)

            lost_fun = 0
            gain_hunger = 0

            pet = Horse(name, typ, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        elif animal == 2:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your eagle has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your eagle's name: " + Colors.ResetAll)
            typ = "Eagle"

            health = randint(50, 75)
            hunger = randint(25, 50)
            fun = randint(50, 75)

            lost_fun = 0
            gain_hunger = 0

            pet = Eagle(name, typ, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        elif animal == 3:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your panther has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your panther's name: " + Colors.ResetAll)
            typ = "Panther"

            health = randint(25, 50)
            hunger = randint(50, 75)
            fun = randint(25, 50)

            lost_fun = 0
            gain_hunger = 0

            pet = Panther(name, typ, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        return pet

    @staticmethod
    def menu():
        global pet
        print("\n")
        option = ""

        while option != "Q":

            print(
                Colors.Bold + Colors.Underlined + Colors.Yellow +
                "----- WELCOME TO  KA'S VIRTUAL PETS ----- \n\n" + Colors.ResetAll +
                " 🦎 🦔 🦨 🐁 🐇 🦅 🐕‍ 🐓 🦞 🐊 🦈 🐍 🦧 🦂 🐶 🐦 🐟\n\n" + Colors.Bold + Colors.Underlined + Colors.Blue +
                "----- MAIN MENU -----"
                + Colors.ResetAll)

            print("""
                N) New game

                C) Continue game 

                L) Load game

                S) Save game

                Q) Exit

                """)

            option = input(Colors.Bold + Colors.Underlined + Colors.Green + "Choose an option: " + Colors.ResetAll)

            if option == "N":
                print("New game")
                Aux.new_game()

            elif option == "C":
                print("Continue game")
                if pet.name == "":
                    print("You don't have a pet!")
                    print("")
                    time.sleep(2)
                else:
                    Aux.continue_game()

            elif option == "L":
                print("Load game")
                Aux.load_game()

            elif option == "S":
                print("Save game")
                if pet.name == "":
                    print("You don't have a pet!")
                    print("")
                    time.sleep(2)
                else:
                    Aux.save()

            elif option == "Q":
                print("Exit")
                pet.stop_threads()
                exit()

            else:
                print(
                    Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)

    @staticmethod
    def new_game():
        global pet
        pet = Aux.hatch()
        Aux.game()

    @staticmethod
    def continue_game():
        global pet
        Aux.game()

    @staticmethod
    def load_game():
        global pet
        opt = 0

        print("Loading game...\n"
              "Slots:\n"
              "1) Slot 1\n"
              "2) Slot 2\n"
              "3) Slot 3\n"
              "4) Slot 4\n"
              "5) Slot 5\n"
              "6) Slot 6\n")

        while opt < 1 or opt > 6:

            opt = int(input("Select the slot where you want to load: "))

            if opt == 1:

                if path1.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT1.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

            elif opt == 2:
                if path2.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT2.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

            elif opt == 3:
                if path3.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT3.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

            elif opt == 4:
                if path4.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT4.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

            elif opt == 5:
                if path5.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT5.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

            elif opt == 6:
                if path6.stat().st_size == 0:
                    print(Colors.Red + Colors.Bold + "Nothing saved here! " + Colors.ResetAll)

                else:

                    with open('SLOT6.json') as file:
                        object = json.load(file)
                        file.close()

                    pet.name = object["name"]
                    pet.type = object["type"]
                    pet.hunger = object["hunger"]
                    pet.health = object["health"]
                    pet.fun = object["fun"]
                    pet.lost_fun = object["lost_fun"]
                    pet.gain_hunger = object["gain_hunger"]
                    pet.time_hatch = object["time_hatch"]

                    Aux.game()

    @staticmethod
    def save():
        opt = 0

        slot["name"] = pet.name
        slot["type"] = pet.type
        slot["hunger"] = pet.hunger
        slot["health"] = pet.health
        slot["fun"] = pet.fun
        slot["lost_fun"] = pet.lost_fun
        slot["gain_hunger"] = pet.gain_hunger
        slot["time_hatch"] = pet.time_hatch

        print("Saving game...\n"
              "Slots:\n"
              "1) Slot 1\n"
              "2) Slot 2\n"
              "3) Slot 3\n"
              "4) Slot 4\n"
              "5) Slot 5\n"
              "6) Slot 6\n")

        while opt < 1 or opt > 6:

            opt = int(input("Select the slot where you want to save the game"))

            if opt == 1:
                with open('SLOT1.json', 'w') as file:
                    json.dump(slot, file)

            elif opt == 2:
                with open('SLOT2.json', 'w') as file:
                    json.dump(slot, file)

            elif opt == 3:
                with open('SLOT3.json', 'w') as file:
                    json.dump(slot, file)

            elif opt == 4:
                with open('SLOT4.json', 'w') as file:
                    json.dump(slot, file)

            elif opt == 5:
                with open('SLOT5.json', 'w') as file:
                    json.dump(slot, file)

            elif opt == 6:
                with open('SLOT6.json', 'w') as file:
                    json.dump(slot, file)

    @staticmethod
    def game():
        global pet
        print(Colors.Bold + Colors.Blue + "Welcome to the game!" + Colors.ResetAll)
        print(
            Colors.Bold + Colors.Blue + "You have a pet named " + Colors.ResetAll + Colors.Bold + Colors.Green +
            pet.name + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)

        pet.start_threads()

        choice = ""

        print(Colors.Bold + Colors.Blue + "GAME STARTED!" + Colors.ResetAll)

        while choice != "4":
            if pet.health <= 0 or pet.hunger >= 100 or pet.fun <= 0:
                print(Colors.Bold + Colors.Red + Colors.Underlined + "Your pet has died!" + Colors.ResetAll)
                Aux.save()
                break

            if pet.health == 100 and pet.hunger == 100 and pet.fun == 100:
                print(
                    Colors.Bold + Colors.Green + Colors.Underlined + "Congratulations! You have a perfect pet!"
                    + Colors.ResetAll)
                Aux.save()
                break

            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.health) + Colors.ResetAll + Colors.Bold + Colors.Blue + " health points. 🫀" + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.hunger) + Colors.ResetAll + Colors.Bold + Colors.Blue + " hunger points. 🍕" + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.fun) + Colors.ResetAll + Colors.Bold + Colors.Blue + " fun points. 😄 " + Colors.ResetAll)

            print("\n")

            print(Colors.Bold + Colors.Underlined + "What would you like to do?" + Colors.ResetAll)
            print(Colors.Bold + Colors.Green + "1. Feed your pet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "2. Play with your pet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Magenta + "3. Visit Vet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Yellow + "4. Return to Main Menu" + Colors.ResetAll)

            choice = input(Colors.Bold + Colors.Blue + "Enter your choice: " + Colors.ResetAll)

            if choice == "1":
                pet.feed()

            elif choice == "2":
                pet.play()

            elif choice == "3":
                pet.vet()

            elif choice == "4":
                pet.stop_threads()
                print(Colors.Bold + Colors.Blue + "Returning to Main Menu......." + Colors.ResetAll)
                Aux.save()
                break

            else:
                print(Colors.Bold + Colors.Red + "Invalid choice!" + Colors.ResetAll)
                continue

            print("\n\n")

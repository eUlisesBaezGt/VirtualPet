from Colors import *
from Pet import *

import json

slot1 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

slot2 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

slot3 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

slot4 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

slot5 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

slot6 = {
    "name": "",
    "type": "",
    "hunger": 0,
    "health": 0,
    "fun": 0,
    "lost_fun": 0,
    "gain_hunger": 0
}

pet = Pet("", "", 0, 0, 0, 0, 0, 0)


def game(pet):
    print(Colors.Bold + Colors.Blue + "Welcome to the game!" + Colors.ResetAll)
    print(
        Colors.Bold + Colors.Blue + "You have a pet named " + Colors.ResetAll + Colors.Bold + Colors.Green + pet.name + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)
    while pet.health > 0 and pet.hunger > 0 and pet.fun > 0:

        print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
            pet.health) + Colors.ResetAll + Colors.Bold + Colors.Blue + " health points." + Colors.ResetAll)
        print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
            pet.hunger) + Colors.ResetAll + Colors.Bold + Colors.Blue + " hunger points." + Colors.ResetAll)
        print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
            pet.fun) + Colors.ResetAll + Colors.Bold + Colors.Blue + " fun points." + Colors.ResetAll)

        print(Colors.Bold + Colors.Blue + "GAME STARTED!" + Colors.ResetAll)

        pet.mk_fun()
        pet.mk_hungry()

        print("\n\n")

        print(Colors.Bold + Colors.Underlined + "What would you like to do?" + Colors.ResetAll)
        print(Colors.Bold + Colors.Green + "1. Feed your pet" + Colors.ResetAll)
        print(Colors.Bold + Colors.Blue + "2. Play with your pet" + Colors.ResetAll)
        print(Colors.Bold + Colors.Magenta + "3. Visit Vet" + Colors.ResetAll)
        print(Colors.Bold + Colors.Yellow + "4. Exit" + Colors.ResetAll)

        choice = input(Colors.Bold + Colors.Blue + "Enter your choice: " + Colors.ResetAll)

        if choice == "1":
            pet.feed()

        elif choice == "2":
            pet.play()

        elif choice == "3":
            pet.vet()

        elif choice == "4":
            print(Colors.Bold + Colors.Blue + "Goodbye!" + Colors.ResetAll)
            save()
            break

        else:
            print(Colors.Bold + Colors.Red + "Invalid choice!" + Colors.ResetAll)
            continue

        print(
            Colors.Bold + Colors.Blue + "Your pet's health is now " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.health) + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)
        print(
            Colors.Bold + Colors.Blue + "Your pet's hunger is now " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.hunger) + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)
        print(
            Colors.Bold + Colors.Blue + "Your pet's fun is now " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.fun) + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)

        print("\n\n")

        if pet.health <= 0:
            print(Colors.Bold + Colors.Red + "Your pet has died!" + Colors.ResetAll)
            save()
            break

        if pet.hunger >= 100:
            print(Colors.Bold + Colors.Red + "Your pet has died!" + Colors.ResetAll)
            save()
            break

        if pet.fun <= 0:
            print(Colors.Bold + Colors.Red + "Your pet has died!" + Colors.ResetAll)
            save()
            break

        if pet.health == 100 and pet.hunger == 100 and pet.fun == 100:
            print(Colors.Bold + Colors.Green + "Congratulations! You have a perfect pet!" + Colors.ResetAll)
            break


def save():
    print(Colors.Bold + Colors.Magenta)
    slot = input("Slot to save? (1-6): ")
    print(Colors.ResetAll)

    if slot == "1":
        print("Slot 1")
        slot1["name"] = pet.name
        slot1["type"] = pet.type
        slot1["hunger"] = pet.hunger
        slot1["health"] = pet.health
        slot1["fun"] = pet.fun
        slot1["lost_fun"] = pet.lost_fun
        slot1["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot1.json', 'w') as file:
            json.dump(slot1, file)

    elif slot == "2":
        print("Slot 2")
        slot2["name"] = pet.name
        slot2["type"] = pet.type
        slot2["hunger"] = pet.hunger
        slot2["health"] = pet.health
        slot2["fun"] = pet.fun
        slot2["lost_fun"] = pet.lost_fun
        slot2["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot2.json', 'w') as file:
            json.dump(slot2, file)

    elif slot == "3":
        print("Slot 3")
        slot3["name"] = pet.name
        slot3["type"] = pet.type
        slot3["hunger"] = pet.hunger
        slot3["health"] = pet.health
        slot3["fun"] = pet.fun
        slot3["lost_fun"] = pet.lost_fun
        slot3["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot3.json', 'w') as file:
            json.dump(slot3, file)

    elif slot == "4":
        print("Slot 4")
        slot4["name"] = pet.name
        slot4["type"] = pet.type
        slot4["hunger"] = pet.hunger
        slot4["health"] = pet.health
        slot4["fun"] = pet.fun
        slot4["lost_fun"] = pet.lost_fun
        slot4["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot4.json', 'w') as file:
            json.dump(slot4, file)

    elif slot == "5":
        print("Slot 5")
        slot5["name"] = pet.name
        slot5["type"] = pet.type
        slot5["hunger"] = pet.hunger
        slot5["health"] = pet.health
        slot5["fun"] = pet.fun
        slot5["lost_fun"] = pet.lost_fun
        slot5["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot5.json', 'w') as file:
            json.dump(slot5, file)

    elif slot == "6":
        print("Slot 6")
        slot6["name"] = pet.name
        slot6["type"] = pet.type
        slot6["hunger"] = pet.hunger
        slot6["health"] = pet.health
        slot6["fun"] = pet.fun
        slot6["lost_fun"] = pet.lost_fun
        slot6["gain_hunger"] = pet.gain_hunger
        slot1["time"] = pet.time

        with open('slot6.json', 'w') as file:
            json.dump(slot6, file)

    else:
        print(
            Colors.Bold + Colors.Underlined + Colors.Red + "Invalid slot number, please try again"
            + Colors.ResetAll)

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

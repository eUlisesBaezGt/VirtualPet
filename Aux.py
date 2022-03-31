from Game import game
from Pet import *
import time

from Colors import *
import json
from random import randint

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
t = 0


class Aux:

    def __init__(self, n_p):
        self.pet = n_p

    @staticmethod
    def print_hatch(tim):
        print(Colors.Bold + Colors.Green + "Your egg will hatch in {} seconds!".format(t) + Colors.ResetAll)
        time.sleep(tim)

    @staticmethod
    def hatch():
        global pet, t
        t = randint(5, 10)
        print("\n")
        print(
            Colors.Bold + Colors.Underlined + Colors.Yellow +
            "----- ANIMALS -----" + Colors.ResetAll)
        print("""
        Horse (EASY MODE) 🐴
        Eagle (MEDIUM MODE) 🦅
        Panther (HARD MODE) 🐯
        """)

        animal = randint(1, 3)

        if animal == 1:
            Aux.print_hatch(t)
            print(Colors.Bold + Colors.Green + "Your horse is ready!" + Colors.ResetAll)
            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your animal's name: ")
            typ = ""

            health = randint(75, 100)
            hunger = randint(0, 25)
            fun = randint(75, 100)

            lost_fun = 0
            gain_hunger = 0
            tem = t
            pet = Horse(name, typ, hunger, health, fun, lost_fun, gain_hunger, tem)

        elif animal == 2:
            Aux.print_hatch(t)
            print(Colors.Bold + Colors.Green + "Your eagle is ready!" + Colors.ResetAll)
            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your animal's name: ")
            typ = ""

            health = randint(50, 75)
            hunger = randint(25, 50)
            fun = randint(50, 75)

            lost_fun = 0
            gain_hunger = 0
            tem = t
            pet = Eagle(name, typ, hunger, health, fun, lost_fun, gain_hunger, tem)

        elif animal == 3:
            Aux.print_hatch(t)
            print(Colors.Bold + Colors.Green + "Your panther is ready!" + Colors.ResetAll)
            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your animal's name: ")
            typ = ""

            health = randint(25, 50)
            hunger = randint(50, 75)
            fun = randint(25, 50)

            lost_fun = 0
            gain_hunger = 0
            tem = t
            pet = Panther(name, typ, hunger, health, fun, lost_fun, gain_hunger, tem)

        return pet

    @staticmethod
    def get_slot(slot):
        if slot == 1:
            return slot1
        elif slot == 2:
            return slot2
        elif slot == 3:
            return slot3
        elif slot == 4:
            return slot4
        elif slot == 5:
            return slot5
        elif slot == 6:
            return slot6
        else:
            return print(
                Colors.Bold + Colors.Underlined + Colors.Red + "Invalid slot number, please try again"
                + Colors.ResetAll)

    @staticmethod
    def slots(slot):
        if slot == slot1:
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

        elif slot == slot2:
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

        elif slot == slot3:
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

        elif slot == slot4:
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

        elif slot == slot5:
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

        elif slot == slot6:
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

    @staticmethod
    def menu():
        print("\n")
        print(
            Colors.Bold + Colors.Underlined + Colors.Yellow +
            "----- WELCOME TO  KA'S VIRTUAL PETS ----- \n\n" + Colors.ResetAll +
            " 🦎 🦔 🦨 🐁 🐇 🦅 🐕‍ 🐓 🦞 🐊 🦈 🐍 🦧 🦂 🐶 🐦 🐟\n\n" +
            Colors.Bold + Colors.Underlined + Colors.Blue +
            "----- MAIN MENU -----"
            + Colors.ResetAll)

        print("""
        N) New game

        C) Continue game 

        L) Load game

        S) Save game

        Q) Exit
        
        """)

        print(Colors.Bold + Colors.Underlined + Colors.Green)
        option = input("Choose an option: ")
        print(Colors.ResetAll)

        if option == "N":
            print("New game")
            Aux.new_game()

        elif option == "C":
            print("Continue game")
            Aux.continue_game()

        elif option == "L":
            print("Load game")
            Aux.load_game()

        elif option == "S":
            print("Save game")
            Aux.save()

        elif option == "Q":
            print("Exit")
            stop_threads()
            Aux.save()
            exit()

        else:
            print(Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)
            Aux.menu()

    @staticmethod
    def new_game():
        g_p = Aux.hatch()
        game(g_p)

    @staticmethod
    def continue_game():
        global pet
        game(pet)

    @staticmethod
    def load_game():
        global pet, slot1, slot2, slot3, slot4, slot5, slot6
        print(Colors.Bold + Colors.Magenta)
        r = int(input("Slot to load? (1-6): "))
        print(Colors.ResetAll)

        if r == 1:
            with open('slot1.json', 'r') as file:
                slot1 = json.load(file)
                pet = Pet(slot1["name"], slot1["type"], slot1["hunger"], slot1["health"], slot1["fun"],
                          slot1["lost_fun"],
                          slot1["gain_hunger"], slot1["time"])
                game(pet)

        elif r == 2:
            with open('slot2.json', 'r') as file:
                slot2 = json.load(file)
                pet = Pet(slot2["name"], slot2["type"], slot2["hunger"], slot2["health"], slot2["fun"],
                          slot2["lost_fun"],
                          slot2["gain_hunger"], slot2["time"])
                game(pet)

        elif r == 3:
            with open('slot3.json', 'r') as file:
                slot3 = json.load(file)
                pet = Pet(slot3["name"], slot3["type"], slot3["hunger"], slot3["health"], slot3["fun"],
                          slot3["lost_fun"],
                          slot3["gain_hunger"], slot3["time"])
                game(pet)

        elif r == 4:
            with open('slot4.json', 'r') as file:
                slot4 = json.load(file)
                pet = Pet(slot4["name"], slot4["type"], slot4["hunger"], slot4["health"], slot4["fun"],
                          slot4["lost_fun"],
                          slot4["gain_hunger"], slot4["time"])
                game(pet)

        elif r == 5:
            with open('slot5.json', 'r') as file:
                slot5 = json.load(file)
                pet = Pet(slot5["name"], slot5["type"], slot5["hunger"], slot5["health"], slot5["fun"],
                          slot5["lost_fun"],
                          slot5["gain_hunger"], slot5["time"])
                game(pet)

        elif r == 6:
            with open('slot6.json', 'r') as file:
                slot6 = json.load(file)
                pet = Pet(slot6["name"], slot6["type"], slot6["hunger"], slot6["health"], slot6["fun"],
                          slot6["lost_fun"],
                          slot6["gain_hunger"], slot6["time"])
                game(pet)

        else:
            print(
                Colors.Bold + Colors.Underlined + Colors.Red + "Invalid slot number, please try again"
                + Colors.ResetAll)
            Aux.load_game()

    @staticmethod
    def save():
        global pet
        print(Colors.Bold + Colors.Magenta)
        r = int(input("Slot to save? (1-6): "))
        print(Colors.ResetAll)
        slot = Aux.get_slot(r)
        Aux.slots(slot)

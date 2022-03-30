from Game import Game
from Pet import Pet

from Colors import *
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


class Aux:
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
        N) New Game # Juego nuevo debe crear el huevo e incubarlo, luego iniciará todos los hilos necesarios.

        C) Continue Game  # Continuar reiniciará los hilos de la mascota (no se puede continuar si no existe mascota)

        L) Load Game # Cargar juego: leerá los datos de la mascota desde un archivo y automáticamente dará inicio 
        a “continuar” el juego. En caso de que ya exista una mascota en juego, lanzar advertencia
    # que perderá los cambios no guardados y si desea continuar.

        S) Save Game #  Guardar juego: escribe todos los datos necesarios, para el correcto funcionamiento del
    # juego, en un archivo.

        Q) Exit # Salir del juego # Salir terminará la ejecución del programa, así como también todos los hilos 
        creados de la mascota.

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
            exit()

        else:
            print(Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)
            Aux.menu()

    @staticmethod
    def new_game():
        pet = Pet.hatch()
        Game(pet)

    @staticmethod
    def continue_game():
        global pet
        Game(pet)

    @staticmethod
    def load_game():
        global pet, slot1, slot2, slot3, slot4, slot5, slot6
        print(Colors.Bold + Colors.Magenta)
        r = int(input("Slot to save? (1-6): "))
        print(Colors.ResetAll)

        if r == 1:
            with open('slot1.json', 'r') as file:
                slot1 = json.load(file)
                pet = Pet(slot1["name"], slot1["type"], slot1["hunger"], slot1["health"], slot1["fun"],
                          slot1["lost_fun"],
                          slot1["gain_hunger"])
                Game(pet)

        elif r == 2:
            with open('slot2.json', 'r') as file:
                slot2 = json.load(file)
                pet = Pet(slot2["name"], slot2["type"], slot2["hunger"], slot2["health"], slot2["fun"],
                          slot2["lost_fun"],
                          slot2["gain_hunger"])
                Game(pet)

        elif r == 3:
            with open('slot3.json', 'r') as file:
                slot3 = json.load(file)
                pet = Pet(slot3["name"], slot3["type"], slot3["hunger"], slot3["health"], slot3["fun"],
                          slot3["lost_fun"],
                          slot3["gain_hunger"])
                Game(pet)

        elif r == 4:
            with open('slot4.json', 'r') as file:
                slot4 = json.load(file)
                pet = Pet(slot4["name"], slot4["type"], slot4["hunger"], slot4["health"], slot4["fun"],
                          slot4["lost_fun"],
                          slot4["gain_hunger"])
                Game(pet)

        elif r == 5:
            with open('slot5.json', 'r') as file:
                slot5 = json.load(file)
                pet = Pet(slot5["name"], slot5["type"], slot5["hunger"], slot5["health"], slot5["fun"],
                          slot5["lost_fun"],
                          slot5["gain_hunger"])
                Game(pet)

        elif r == 6:
            with open('slot6.json', 'r') as file:
                slot6 = json.load(file)
                pet = Pet(slot6["name"], slot6["type"], slot6["hunger"], slot6["health"], slot6["fun"],
                          slot6["lost_fun"],
                          slot6["gain_hunger"])
                Game(pet)

        else:
            print(
                Colors.Bold + Colors.Underlined + Colors.Red + "Invalid slot number, please try again" + Colors.ResetAll)
            Aux.load_game()

    @staticmethod
    def save():
        global pet
        print(Colors.Bold + Colors.Magenta)
        r = int(input("Slot to save? (1-6): "))
        print(Colors.ResetAll)
        slot = Aux.get_slot(r)
        Aux.slots(slot)

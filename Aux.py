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

    L) Load Game # Cargar juego: leerá los datos de la mascota desde un archivo y automáticamente dará inicio a “continuar” el juego. En caso de que ya exista una mascota en juego, lanzar advertencia
# que perderá los cambios no guardados y si desea continuar.

    S) Save Game #  Guardar juego: escribe todos los datos necesarios, para el correcto funcionamiento del
# juego, en un archivo.

    Q) Exit # Salir del juego # Salir terminará la ejecución del programa, así como también todos los hilos creados de la mascota.

    """)

    print(Colors.Bold + Colors.Underlined + Colors.Green)
    option = input("Choose an option: ")
    print(Colors.ResetAll)

    if option == "N":
        print("New game")
        new_game()

    elif option == "C":
        print("Continue game")
        continue_game()

    elif option == "L":
        print("Load game")
        load_game()

    elif option == "S":
        print("Save game")
        save()

    elif option == "Q":
        print("Exit")
        exit()

    else:
        print(Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)
        menu()


def slots(n):
    if n == 1:
        slot1["name"] = pet.name
        slot1["type"] = pet.type
        slot1["hunger"] = pet.hunger
        slot1["health"] = pet.health
        slot1["fun"] = pet.fun
        slot1["lost_fun"] = pet.lost_fun
        slot1["gain_hunger"] = pet.gain_hunger

        with open('slot1.json', 'w') as file:
            json.dump(slot1, file)

    elif n == 2:
        slot2["name"] = pet.name
        slot2["type"] = pet.type
        slot2["hunger"] = pet.hunger
        slot2["health"] = pet.health
        slot2["fun"] = pet.fun
        slot2["lost_fun"] = pet.lost_fun
        slot2["gain_hunger"] = pet.gain_hunger

        with open('slot2.json', 'w') as file:
            json.dump(slot2, file)

    elif n == 3:
        slot3["name"] = pet.name
        slot3["type"] = pet.type
        slot3["hunger"] = pet.hunger
        slot3["health"] = pet.health
        slot3["fun"] = pet.fun
        slot3["lost_fun"] = pet.lost_fun
        slot3["gain_hunger"] = pet.gain_hunger

        with open('slot3.json', 'w') as file:
            json.dump(slot3, file)

    elif n == 4:
        slot4["name"] = pet.name
        slot4["type"] = pet.type
        slot4["hunger"] = pet.hunger
        slot4["health"] = pet.health
        slot4["fun"] = pet.fun
        slot4["lost_fun"] = pet.lost_fun
        slot4["gain_hunger"] = pet.gain_hunger

        with open('slot4.json', 'w') as file:
            json.dump(slot4, file)

    elif n == 5:
        slot5["name"] = pet.name
        slot5["type"] = pet.type
        slot5["hunger"] = pet.hunger
        slot5["health"] = pet.health
        slot5["fun"] = pet.fun
        slot5["lost_fun"] = pet.lost_fun
        slot5["gain_hunger"] = pet.gain_hunger

        with open('slot5.json', 'w') as file:
            json.dump(slot5, file)

    elif n == 6:
        slot6["name"] = pet.name
        slot6["type"] = pet.type
        slot6["hunger"] = pet.hunger
        slot6["health"] = pet.health
        slot6["fun"] = pet.fun
        slot6["lost_fun"] = pet.lost_fun
        slot6["gain_hunger"] = pet.gain_hunger

        with open('slot6.json', 'w') as file:
            json.dump(slot6, file)


def save():
    global pet
    print(Colors.Bold + Colors.Magenta)
    r = int(input("Slot to save? (1-6)"))
    print(Colors.ResetAll)

    if r == 1:
        slots(1)

    elif r == 2:
        slots(2)

    elif r == 3:
        slots(3)

    elif r == 4:
        slots(4)

    elif r == 5:
        slots(5)

    elif r == 6:
        slots(6)

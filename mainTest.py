from Pet import *
from Aux import Aux


def stop_threads():
    pass


def load_game():
    global saved
    global pet

    with open("log.txt", "r") as file:
        data = file.read()
        if data == "":
            print("No data saved")

        else:
            if saved:
                splitter()

            else:
                print("You have unsaved data, if you continue you will lose it")
                choice = input("Do you want to continue? (y/n)")
                if choice == "y":
                    splitter()
                else:
                    print("game will not continue")
    continue_game()


def splitter():
    global pet, data
    pet.name = data.split("\n")[0]
    pet.type = data.split("\n")[1]
    pet.hunger = int(data.split("\n")[2])
    pet.health = int(data.split("\n")[3])
    pet.fun = int(data.split("\n")[4])
    pet.lost_fun = int(data.split("\n")[5])
    pet.gain_hunger = int(data.split("\n")[6])


def continue_game():
    global pet
    game()
    # Continuar reiniciará los hilos de la mascota (no se puede continuar si no existe mascota)


def new_game():
    hatch()
    game()

def hatch():
    global pet
    pet = Pet()


def game():
    global pet
    global saved
    saved = False

def save():
    global pet
    global saved
    with open("log.txt", "w") as file:
        file.write(pet.name + "\n")
        file.write(pet.type + "\n")
        file.write(str(pet.hunger) + "\n")
        file.write(str(pet.health) + "\n")
        file.write(str(pet.fun) + "\n")
        file.write(str(pet.lost_fun) + "\n")
        file.write(str(pet.gain_hunger) + "\n")
    saved = True


created = False
saved = False
pet = Pet("", "", 0, 0)
data = ""

while True:
    print("N) New game")  # Juego nuevo debe crear el huevo e incubarlo, luego iniciará todos los hilos necesarios.
    print("C) continue")
    print("L) Load game")
    print("S) save")
    print("Q) Exit")
    option = input("Choose an option: ")

    if option == "N":
        print("New game")
        new_game()
        created = True

    elif option == "C":
        print("Continue")
        if created:
            continue_game()
        else:
            print("No game created")

    elif option == "L":
        print("Load game")
        if created and saved:
            load_game()
        else:
            print("No game created or saved")

    elif option == "S":
        print("Saving")
        if created:
            save()
        else:
            print("No game created")

    elif option == "Q":
        print("Exit")  # Salir terminará todos los hilos creados de la mascota.
        stop_threads()
        break

    else:
        print("Invalid option")

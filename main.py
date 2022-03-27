# from Pet import *
# from Aux import Aux


def stop_threads():
    pass


def load_game():
    # Cargar juego: y automáticamente dará inicio
    # a “continuar” el juego. En caso de que ya exista una mascota en juego, lanzar advertencia
    # que perderá los cambios no guardados y si desea continuar.

    with open("log.txt", "r") as file:
        data = file.read()
        if data == "":
            print("No hay datos guardados")
        else:
            continue_game()


def continue_game():
    # Continuar reiniciará los hilos de la mascota (no se puede continuar si no existe mascota)

    with open("log.txt", "r") as file:
        data = file.read()
        if data == "":
            print("No hay datos guardados")
        else:
            _name = data.split("\n")[0]
            _type = data.split("\n")[1]
            _hunger = int(data.split("\n")[2])
            _health = int(data.split("\n")[3])
            _fun = int(data.split("\n")[4])

            # add lostFun and gainFun hunger


def new_game():
    pass


def save(pet):
    with open("log.txt", "w") as file:
        file.write(pet.name + "\n")
        file.write(pet.type + "\n")
        file.write(str(pet.hunger) + "\n")
        file.write(str(pet.health) + "\n")
        file.write(str(pet.fun) + "\n")

        file.write("" + "\n")  # __lost_fun
        file.write("" + "\n")  # __gain_hunger


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
    elif option == "C":
        print("continue")
        continue_game()
    elif option == "L":
        print("Load game")
        load_game()
    elif option == "S":
        print("save")
        # save()
    elif option == "Q":
        print("Exit")  # Salir terminará todos los hilos creados de la mascota.
        stop_threads()
        break
    else:
        print("Invalid option")

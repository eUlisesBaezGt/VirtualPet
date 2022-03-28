import Print as Print

from Colors import *
from Pet import *
from Aux import *


def menu():
    print("\n")
    print(
        Colors.Bold + Colors.Underlined + Colors.Yellow +
        "----- WELCOME TO  KA'S VIRTUAL PETS ----- \n\n" + Colors.ResetALl +
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

    print(Colors.Bold + Colors.Underlined + Colors.Green + "")
    option = input("Choose an option: ")
    print("" + Colors.ResetAll)

    if option == "N":
        print("New game")
        new_game()
        created = True

    elif option == "C":
        print("Continue game")
        continue_game()
        created = True

    elif option == "L":
        print("Load game")
        load_game()
        created = True

    elif option == "S":
        print("Save game")
        save_game()
        created = True

    elif option == "Q":
        print("Exit")
        exit()

    else:
        print(Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)
        menu()


if __name__ == "__main__":
    menu()

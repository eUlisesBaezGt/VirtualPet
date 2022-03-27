from Pet import *
from Aux import Aux

def stop_threads():
    pass


while True:
    print("N) New game") # Juego nuevo debe crear el huevo e incubarlo, luego iniciará todos los hilos necesarios.
    print("C) Continue") # Continuar reiniciará los hilos de la mascota (no se puede continuar si no existe mascota)
    print("L) Load game") # Cargar juego: leerá los datos de la mascota desde un archivo y automáticamente dará inicio
    # a “continuar” el juego. En caso de que ya exista una mascota en juego, lanzar advertencia
    # que perderá los cambios no guardados y si desea continuar.
    print("S) Save") # Guardar juego: escribe todos los datos necesarios, para el correcto funcionamiento del
    # juego, en un archivo.
    print("Q) Exit")
    option = input("Choose an option: ")
    if option == "N":
        print("New game")
    elif option == "C":
        print("Continue")
    elif option == "L":
        print("Load game")
    elif option == "S":
        print("Save")
    elif option == "Q":
        print("Exit")
        # Salir terminará todos los hilos creados de la mascota.
        stop_threads()
        break
    else:
        print("Invalid option")

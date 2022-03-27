from Colors import *
from Pet import *
from Aux import *


def menu():
    print("\n")
    print(Colors.Bold + Colors.Underlined + Colors.Yellow +
          "----- WELCOME TO  KA'S VIRTUAL PETS ----- \n\n" +
          Colors.ResetALl +
          " 🦎 🦔 🦨 🐁 🐇 🦅 🐕‍ 🐓 🦞 🐊 🦈 🐍 🦧 🦂 🐶 🐦 🐟\n\n" +
          Colors.Bold + Colors.Underlined + Colors.Blue +
          "----- MAIN MENU -----"
          + Colors.ResetALl)

    print("""
    1. New Game # Juego nuevo debe crear el huevo e incubarlo, luego iniciará todos los hilos necesarios.
    
    2. Continue Game  # Continuar reiniciará los hilos de la mascota (no se puede continuar si no existe mascota)
    
    3. Load Game # Cargar juego: leerá los datos de la mascota desde un archivo y automáticamente dará inicio a “continuar” el juego. En caso de que ya exista una mascota en juego, lanzar advertencia
# que perderá los cambios no guardados y si desea continuar.

    4. Save Game #  Guardar juego: escribe todos los datos necesarios, para el correcto funcionamiento del
# juego, en un archivo.
    
    5. Exit # Salir del juego # Salir terminará la ejecución del programa, así como también todos los hilos creados de la mascota.

    """)


if __name__ == "__main__":
    menu()

import option as option
from Pet import *
import time
from Colors import *
import json
from random import randint


class Aux:
    pet = Pet()

    def __init__(self, pet):
        self.pet = pet

    @staticmethod
    def print_hatch(time_hatch):
        print(Colors.Bold + Colors.Green + "Your egg will hatch in {time_hatch} seconds!" + Colors.ResetAll)
        for i in range(time_hatch):
            print("\n")
            print(
                Colors.Bold + Colors.Green + "Your egg is hatching! {time_hatch - i} seconds left!....." +
                Colors.ResetAll)
            time.sleep(1)

    @staticmethod
    def hatch():
        global pet
        time_hatch = randint(5, 10)
        print(
            Colors.Bold + Colors.Underlined + Colors.Yellow + "----- ANIMALS -----" + Colors.ResetAll)
        print("""
        Horse (EASY MODE) 🐴
        Eagle (MEDIUM MODE) 🦅
        Panther (HARD MODE) 🐯
            """)

        animal = randint(1, 3)

        if animal == 1:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your horse has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your horse's name: " + Colors.ResetAll)
            type = "Horse"

            health = randint(75, 100)
            hunger = randint(0, 25)
            fun = randint(75, 100)

            lost_fun = 0
            gain_hunger = 0

            pet = Horse(name, type, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        elif animal == 2:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your eagle has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your eagle's name: " + Colors.ResetAll)
            type = "Eagle"

            health = randint(50, 75)
            hunger = randint(25, 50)
            fun = randint(50, 75)

            lost_fun = 0
            gain_hunger = 0

            pet = Eagle(name, type, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        elif animal == 3:
            Aux.print_hatch(time_hatch)
            print(Colors.Bold + Colors.Green + "Your panther has hatched!\n" + Colors.ResetAll)

            name = input(Colors.Bold + Colors.Blue + Colors.Underlined + "Your panther's name: " + Colors.ResetAll)
            type = "Panther"

            health = randint(25, 50)
            hunger = randint(50, 75)
            fun = randint(25, 50)

            lost_fun = 0
            gain_hunger = 0

            pet = Panther(name, type, hunger, health, fun, lost_fun, gain_hunger, time_hatch)

        return pet

    @staticmethod
    def menu():
        print("\n")
        option = ""

        while option != "Q":

            print(
                Colors.Bold + Colors.Underlined + Colors.Yellow +
                "----- WELCOME TO  KA'S VIRTUAL PETS ----- \n\n" + Colors.ResetAll +
                " 🦎 🦔 🦨 🐁 🐇 🦅 🐕‍ 🐓 🦞 🐊 🦈 🐍 🦧 🦂 🐶 🐦 🐟\n\n" + Colors.Bold + Colors.Underlined + Colors.Blue +
                "----- MAIN MENU -----"
                + Colors.ResetAll)

            print("""
                N) New game
    
                C) Continue game 
    
                L) Load game
    
                S) Save game
    
                Q) Exit
    
                """)

            option = input(Colors.Bold + Colors.Underlined + Colors.Green + "Choose an option: " + Colors.ResetAll)

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
                print(
                    Colors.Bold + Colors.Underlined + Colors.Red + "Invalid input, please try again" + Colors.ResetAll)

    @staticmethod
    def new_game():
        pet = Aux.hatch()
        Aux.game(pet)

    @staticmethod
    def continue_game():
        global pet
        Aux.game(pet)

    @staticmethod
    def game(pet):
        print(Colors.Bold + Colors.Blue + "Welcome to the game!" + Colors.ResetAll)
        print(
            Colors.Bold + Colors.Blue + "You have a pet named " + Colors.ResetAll + Colors.Bold + Colors.Green +
            pet.name + Colors.ResetAll + Colors.Bold + Colors.Blue + "." + Colors.ResetAll)

        pet.mk_fun()
        pet.mk_hungry()

        choice = ""

        print(Colors.Bold + Colors.Blue + "GAME STARTED!" + Colors.ResetAll)

        while choice != "4":
            if pet.health <= 0 or pet.hunger >= 100 or pet.fun <= 0:
                print(Colors.Bold + Colors.Red + Colors.Underlined + "Your pet has died!" + Colors.ResetAll)
                Aux.save()
                break

            if pet.health == 100 and pet.hunger == 100 and pet.fun == 100:
                print(
                    Colors.Bold + Colors.Green + Colors.Underlined + "Congratulations! You have a perfect pet!" + Colors.ResetAll)
                Aux.save()
                break

            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.health) + Colors.ResetAll + Colors.Bold + Colors.Blue + " health points." + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.hunger) + Colors.ResetAll + Colors.Bold + Colors.Blue + " hunger points." + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "You have " + Colors.ResetAll + Colors.Bold + Colors.Green + str(
                pet.fun) + Colors.ResetAll + Colors.Bold + Colors.Blue + " fun points." + Colors.ResetAll)

            print("\n")

            print(Colors.Bold + Colors.Underlined + "What would you like to do?" + Colors.ResetAll)
            print(Colors.Bold + Colors.Green + "1. Feed your pet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Blue + "2. Play with your pet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Magenta + "3. Visit Vet" + Colors.ResetAll)
            print(Colors.Bold + Colors.Yellow + "4. Return to Main Menu" + Colors.ResetAll)

            choice = input(Colors.Bold + Colors.Blue + "Enter your choice: " + Colors.ResetAll)

            if choice == "1":
                pet.feed()

            elif choice == "2":
                pet.play()

            elif choice == "3":
                pet.vet()

            elif choice == "4":
                stop_threads()
                print(Colors.Bold + Colors.Blue + "Returning to Main Menu......." + Colors.ResetAll)
                Aux.save()
                break

            else:
                print(Colors.Bold + Colors.Red + "Invalid choice!" + Colors.ResetAll)
                continue

            print("\n\n")

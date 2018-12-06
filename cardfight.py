#!/usr/bin/env python3

#from functions import *
import functions
from time import sleep
def main():
    PokeDict = defaultPokeDict()
    menu()

Lvl=functions.getLevel()
XP=functions.getXP()
#Default Dict if we don't load one
def defaultPokeDict():
    PokeDict = [
         { "level": 1, "name": "Bulbasaur", "health": 200, "attack": 8, "description": "The Grass Pokemon",},
         { "level": 1, "name": "Charmander", "health": 160, "attack": 10, "description": "The Fire Pokemon",},
         { "level": 1, "name": "Squirtle", "health": 180, "attack": 9, "description": "The Water Pokemon", },
         { "level": 3, "name": "Ivysaur", "health": 240, "attack": 11, "description": "The Evolved Grass Pokemon",},
         { "level": 3, "name": "Charmelion", "health": 220, "attack": 13, "description": "The Evoled Fire Pokemon",},
         { "level": 3, "name": "Wartortle", "health": 230, "attack": 12, "description": "The Evolved Water Pokemon",},
    ]
    return(PokeDict)

#Main Menu #TODO make menu take a list of options
def menu():
    while True:
        try:
            print("1) Load Character deck from file")
            print("2) Save current Character deck")
            print("3) Show your stats")
            print("4) Choose your opponent and Fight!")
            print("5) Exit!")
            choice = int(input('Make Your Choice:'))
            print("You selected: ",choice)
            if   choice == 1:
                PokeDict=functions.LoadPokedex()
            elif choice == 2:
                functions.SavePokedex(PokeDict)
            elif choice == 3:
                functions.ReadStats()
            elif choice == 4:
                functions.SelectOpponent(PokeDict)
            elif choice == 5:
                exit()
            else:
                print("We didn't really get here!")
        except ValueError:
            print ("Oops! That was not a valid number. Try again...")
        except IndexError:
            print ("Oh dear! That number isn't a choice. Please try again") 

name="__main__"
print("Welcome to the Trading Card fighting simulator!")
sleep(1)

main()

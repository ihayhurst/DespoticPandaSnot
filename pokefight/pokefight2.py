#!/usr/bin/env python3

from functions import *
import time

Lvl=100
XP=0
#Default Dict if we don't load one
PokeDict = [
      { "level": 1, "name": "Bulbasaur", "health": 200, "attack": 8, "description": "The Grass Pokemon" },
      { "level": 1, "name": "Charmander", "health": 160, "attack": 10, "description": "The Fire Pokemon" },
      { "level": 1, "name": "Squirtle", "health": 180, "attack": 9, "description": "The Water Pokemon" },
      { "level": 3, "name": "Ivysaur", "health": 240, "attack": 11, "description": "The Evolved Grass Pokemon" },
      { "level": 3, "name": "Charmelion", "health": 220, "attack": 13, "description": "The Evoled Fire Pokemon"},
      { "level": 3, "name": "Wartortle", "health": 230, "attack": 12, "description": "The Evolved Water Pokemon"},
]
## --- Main Prog start --- ##
print ("Welcome to the pokemon fighting simulator!")
time.sleep(1)
print ("Your are Level",Lvl)
time.sleep(0.3)
print ("Your XP is:",XP)
time.sleep(0.3)

#Main Menu #TODO make menu a function
while True:
    try:
        print("1) Load Pokedex from file")
        print("2) Save current Pokedex")
        print("3) Choose your opponent and  Fight!")
        print("4) Exit!")
        choice = int(input('Make Your Choice:'))
        print("You selected: ",choice)
        if    choice == 1:
            PokeDict=LoadPokedex()
        elif  choice == 2:
            SavePokedex(PokeDict)
        elif  choice == 3:
            SelectOpponent(PokeDict)
        elif  choice == 4:
            exit()
        else:
          print("We didn't really get here!")
          break
    except ValueError:
                print ("Oops! That was not a valid number. Try again...")
    except IndexError:
                print ("Oh dear! That number isn't a choice. Please try again") 



#!/usr/bin/env python3

from functions import *
import time

Lvl=100
XP=0
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
        print("2) Save Standard Pokedex as template")
        print("3) Choose your opponent and  Fight!")
        print("4) Exit!")
        choice = int(input('Make Your Choice:'))
        print("You selected: ",choice)
        if    choice == 1:
            LoadPokedex()
        elif  choice == 2:
            SavePokedex()
        elif  choice == 3:
            SelectOpponent()
        elif  choice == 4:
            exit()
        else:
          print("We didn't really get here!")
          break
    except ValueError:
                print ("Oops! That was not a valid number. Try again...")
    except IndexError:
                print ("Oh dear! That number isn't a choice. Please try again") 



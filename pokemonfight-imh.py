#!/usr/bin/env python


#Modules

import time
import random
import sys

#Variables

Lvl=1

PokeDict = [
	 { "level": 1, "name": "Bulbasaur", "health": 100, "attack": 7, "description": "The Grass Pokemon" },
	 { "level": 1, "name": "Charmander", "health": 80, "attack": 9, "description": "The Fire Pokemon" },
	 { "level": 1, "name": "Squirtle", "health": 90, "attack": 8, "description": "The Water Pokemon" },
	 { "level": 2, "name": "Wobblybottom", "health": 100, "attack": 11, "description": "The 'likes his food' Pokemon" },
]



## --- Main Prog start --- ##
print ("Welcome to the pokemon fighting simulator!")
time.sleep(1)
print ("Here you will choose a starter Pokemon")

print ("-"*40)
time.sleep(0.3)

#generate list for your level
choices=[]
for s in PokeDict:
    if s['level'] == Lvl:
        choices.append(s)

#print menu from  (choices)
for idx, li in enumerate(choices):
  print ("For ",li['name'],li['description'], "press ",idx )

print ("-"*40)

#make choice and check it is valid
while True:
	try:
		choice = int(input('Make Your Choice:'))
		MyPokemon = (choices[choice])
		break
	except ValueError:
	   	print ("Oops!  That was no valid number.  Try again...")
	except IndexError:
		print ("Oh dear! That number isn't a choice. Please try again")

#Report choice and setup choice variables
print ("="*10, " You chose ",MyPokemon['name'], " ","="*10)
print (MyPokemon['name'], " is great choice!", MyPokemon['description'])
print ("He has Health: ", MyPokemon['health'], "and attack", MyPokemon['attack'])
MyPokemonHealth = MyPokemon['health']
MyPokemonAttack = MyPokemon['attack']



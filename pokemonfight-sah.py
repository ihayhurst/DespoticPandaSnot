#!/usr/bin/env python3


#Modules

import time
import random
import sys

#Variables

MyAttack=1
MyHealth=1
EnemyHealth=100
Xp=10
Lvl=1
valid = False

def SetMyPokemon(choice):
	print (choice)
	if choice =='Bulbasaur':
		MyHealth = 100; MyAttack = 7
	elif choice == 'Charmander':
		MyHealth = 80; MyAttack = 9
	elif choice == 'Squirtle':
		MyHealth = 90; MyAttack = 8
	return MyHealth, MyAttack

print ("Welcome to the pokemon fighting simulator!")
time.sleep(1)
print ("Here you will choose a starter Pokemon")

print ("-"*40)
time.sleep(0.3)
print ("Bulbasaur - The Grass Pokemon - Health:100 Attack:7 - Press 1 to select him.")
time.sleep(0.3)
print ("Charmander - The Fire Pokemon - Health:80 Attack:9 - Press 2 to select him.")
time.sleep(0.3)
print ("Squirtle - The Water Pokemon - Health:90 Attack:8  - Press 3 to select him.")
time.sleep(0.5)
while True:
	choice = input('Make Your Choice:')
	if valid:  break
	elif choice == '1':
		SetMyPokemon("Bulbasaur")
		break	
	elif choice == '2':
		SetMyPokemon("Charmander")
		break
	elif choice == '3':
		SetMyPokemon("Squirtle")
		break
	else:
		 print ("Please make a valid selection")

print ("-"*40)
print ("Great Choice!")
print (choice)
print ("Heatlth: ",MyHealth)
print ("Attack: ",MyAttack)
print (SetMyPokemon('Bulbasaur'))

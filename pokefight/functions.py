#!/usr/bin/env python3


#Modules
import time
import random
import sys
import json

#Variables

Lvl=100
XP=0 
#The amount of xp to level up will increase by each level. Xp will need to be put into another file to save it.
'''#Default Dict if we don't load one 
PokeDict = [
     { "level": 1, "name": "Bulbasaur", "health": 200, "attack": 8, "description": "The Grass Pokemon" },
     { "level": 1, "name": "Charmander", "health": 160, "attack": 10, "description": "The Fire Pokemon" },
     { "level": 1, "name": "Squirtle", "health": 180, "attack": 9, "description": "The Water Pokemon" },
     { "level": 3, "name": "Ivysaur", "health": 240, "attack": 11, "description": "The Evolved Grass Pokemon" },
     { "level": 3, "name": "Charmelion", "health": 220, "attack": 13, "description": "The Evoled Fire Pokemon"},
     { "level": 3, "name": "Wartortle", "health": 230, "attack": 12, "description": "The Evolved Water Pokemon"},
]
'''
def fight(health,attack):
    damage = 0
    hit=random.randint(0,100)
    damage = (hit * 0.02) * attack
    damage = int(damage)
    health = health - damage
    print (health)
    print ("Damage inflicted:",damage)
    return health


def LoadPokedex():
    print("Loading opponent file...")
    with open("PokeDict2.json", "r") as read_file:
         PokeDict = json.load(read_file)
   # with open('PokeDict2.json', 'r') as fp:
   #     PokeDict = json.load(fp)
   # with open('PokeDict2.json') as handle:
   #    PokeDict = json.loads(handle.read())
    time.sleep(2)
    return PokeDict

def SavePokedex():
    print("Saving Pokedex...")
    with open("PokeDict.json", "w") as write_file:
        json.dump(PokeDict, write_file, indent=4)
    time.sleep(3)
    return

def SelectOpponent(PokeDict):
    print ("Here you will choose your Pokemon")

    print ("-"*30)
    time.sleep(0.3)

    #generate list for your level
    choices=[]
    for s in PokeDict:
        if s['level'] <= Lvl:
            choices.append(s)

    #print menu from  (choices)
    for idx, li in enumerate(choices):
        print (idx,") ",bcolors.BOLD+li['name'],bcolors.ENDC+" - ",li['description'],"\n    Health:",li['health'],"Attack:",li['attack'])
        print ("-"*30)

    #make choice and check it is valid
    while True:
        try:
            choice = int(input('Make Your Choice:'))
            MyPokemon = (choices[choice])
            break
        except ValueError:
            print ("Oops! That was not a valid number. Try again...")
        except IndexError:
            print ("Oh dear! That number isn't a choice. Please try again")

    #Report choice and setup choice variables
    print ("="*10, " You chose",MyPokemon['name'], " ","="*10)
    print (MyPokemon['name'], "is a  great choice!", MyPokemon['description'])
    print ("His stats are: Health:", MyPokemon['health'], "Attack:", MyPokemon['attack'])
    MyPokemonHealth = MyPokemon['health']
    MyPokemonAttack = MyPokemon['attack']

    #Select eneny Pokemon
    EnemyLevel= MyPokemon['level']
    EnemyChoices=[]
    for s in PokeDict:
        if s['level'] == EnemyLevel:
            EnemyChoices.append(s)

    Maxidx=len(EnemyChoices)
    #print(Maxidx)
    EnemyChoice =random.randint(0,Maxidx-1)

    #print (EnemyChoice)
    EnemyPokemon = (EnemyChoices[EnemyChoice])
    print ("Your opponent is",EnemyPokemon['name'])
    EnemyPokemonHealth = EnemyPokemon['health']
    EnemyPokemonAttack = EnemyPokemon['attack'] 

    #Fighting
    for rounds in range(1,100):


        if random.randint(0,1):
            #You attack
            print ("Round", rounds)
            input("Press Return To Attack")
            print ("Enemy health:")
            EnemyPokemonHealth = fight(EnemyPokemonHealth,MyPokemonAttack)
            if EnemyPokemonHealth <= 0: break
            #Opponent attacks
            print ("Your Health")
            MyPokemonHealth = fight(MyPokemonHealth,EnemyPokemonAttack)
            if MyPokemonHealth <= 0: break
            print ("-"*30)
        else:
            #Opponent Attacks
            print ("Round", rounds)
            print ("Your Health")
            MyPokemonHealth = fight(MyPokemonHealth,EnemyPokemonAttack)
            if MyPokemonHealth <= 0: break
            #You attack
            input("Press Return To Attack")
            print ("Enemy Health")
            EnemyPokemonHealth = fight(EnemyPokemonHealth,MyPokemonAttack)
            if EnemyPokemonHealth <= 0: break
            print ("-"*30)

    #Detect Winner
    if MyPokemonHealth > EnemyPokemonHealth:
        print ("You win!")
    else:
        print ("Your Opponent won!")    

    print (rounds,"rounds")
    print ("Your Health is",MyPokemonHealth,"Your Opponents Health is",EnemyPokemonHealth)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

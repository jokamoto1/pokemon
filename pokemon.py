import math
import random
import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, moves,  attack , defense, health):
        self.name = name
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.health = health
    
    def fight(self , opponent):
        print("\n"*70)
        print("-----------POKEMONE BATTLE-----------")
        print("\n")
        delay_print(f"\nFight Between {self.name} and {opponent.name}")
        while (self.health > 0 and opponent.health > 0):

            delay_print(f"\n{self.name}'s Health: {self.health} ") 

            delay_print(f"\n{opponent.name}'s Health: {opponent.health} ") 

            print("\n")
            print("-------------------------------------")
            print("\n")
            delay_print(f"\n{self.name}'s turn!")
            print("\n")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x) 
            print("\n")
            index = int(input("Pick a move:"))    
            if index == 1:
                self.attack *= 1.5
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            damage = math.floor(self.attack * random.uniform(1 , 1.5)) - opponent.defense
            print("\n")
            if index == 1:
                damage = 0
            if damage == 0:
                delay_print(f"{self.name} increased their attack!")
            elif damage >= 5:
                delay_print("It was super effective!")
            elif damage < 5 and damage > 3:
                delay_print("It was effective!")
            elif damage <= 3:
                delay_print("It was not very effecive!")
            if damage <= 0: 
                damage = 0
            print("\n")
            opponent.health -= damage
            delay_print(f"\n{opponent.name} took {damage} damage!")
            if opponent.health <= 0:
                print("\n")
                print("-------------------------------------")
                delay_print(f"\n{opponent.name} lost!")
                print("\n")
                print("-------------------------------------")
                break

            print("\n")
            delay_print(f"\n{opponent.name}'s turn!")
            print("\n")
            for i, x in enumerate(opponent.moves):
                print(f"{i+1}.", x) 
            print("\n")
            index = int(input("Pick a move:"))
            if index == 1:
    
                opponent.attack *= 1.5
       
            delay_print(f"\n{opponent.name} used {opponent.moves[index-1]}!")
            damage = math.floor(opponent.attack * random.uniform(1 , 1.5)) - self.defense
            print("\n")
            if index == 1:
                damage = 0
            if damage == 0:
                delay_print(f"{opponent.name} increased their attack!")
            elif damage >= 5:
                delay_print("It was super effective!")
            elif damage < 5 and damage > 2:
                delay_print("It was effective!")
            elif damage <= 2:
                delay_print("It was not very effecive!")
            if damage <= 0: 
                damage = 0
            print("\n")
            self.health -= damage
            delay_print(f"\n{self.name} took {damage} damage!")
            print("\n")
            delay_print("---------------New Turn--------------") 
            print("\n")
           

            if self.health <= 0:
                print("\n")
                print("-------------------------------------")
                delay_print(f"\n{self.name} lost!")
                print("\n")
                print("-------------------------------------")
        
                break
if __name__ == '__main__':
    Charmander = Pokemon('Charmander', ['Boost (INCREASE ATK)', 'Scratch', 'Tackle', 'Fire Punch'],4,2 ,10)
    Squirtle = Pokemon('Squirtle',  ['Boost (INCREASE ATK)', 'Tackle', 'Headbutt', 'Surf'], 3, 3 ,10)
    Bulbasaur = Pokemon('Bulbasaur',  ['Boost (INCREASE ATK)', 'Razor Leaf', 'Tackle', 'Leech Seed'], 2,4 ,10)

Charmander.fight(Squirtle)

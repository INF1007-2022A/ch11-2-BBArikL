"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker: Character, defender: Character):
	attacker.compute_damage(defender)

def run_battle(c1, c2):
	tours = 0
	print(f"{c1.name} starts a battle with {c2.name}!")
	while c1.hp > 0 and c2.hp > 0:
		attacker, defender = (c1, c2) if tours % 2 == 0 else (c2, c1)
		deal_damage(attacker, defender)
		tours += 1

	dead_character = c1 if c1.hp <= 0 else c2

	print(f"{dead_character.name} is sleeping with the fishes.")


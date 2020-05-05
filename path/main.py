#!/usr/bin/env python3.8

import os, sys
import story
import world
import woods


path = os.path.dirname(os.path.realpath(__file__))


def Warrior(hero):
    filename = (path + "/warrior.txt")
    myChoice = int(story.read(filename, 5, hero))
    wood(hero, Weapon(myChoice))


def Weapon(myChoice):
    return {
        1 : ['long sword', 'warrior'],
        2 : ['sword & shield', 'paladin'],
        3 : ['dagger', 'thief'],
        4 : ['mace', 'cleric'],
        5 : ['bow', 'ranger'],
    }.get(myChoice, 'You died') 

    
def Arcane(hero):
    filename = (path + "/arcane.txt")
    myChoice = int(story.read(filename, 5, hero))
    wood(hero, ArcaneWeapon(myChoice))


def ArcaneWeapon(myChoice):
    return {
        1 : ['wand', 'mage'],
        2 : ['cauldron', 'witch & warlock'],
        3 : ['skull', 'necromancer'],
    }.get(myChoice, 'You died') 


def wood(hero, weapon):
    hero['weapon'] = weapon[0]
    hero['class'] = weapon[1]
    filename = (path + "/wood.txt")
    story.read(filename, None, hero)
    woods.fork(hero)

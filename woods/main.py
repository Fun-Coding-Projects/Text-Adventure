import story
import os
import path

path = os.path.dirname(os.path.realpath(__file__))
cwd = os.path.dirname(__file__)

def fork(hero):
    filename = os.path.join(cwd, 'intro.txt')
    myChoice = story.read(filename, 2, hero)
    if myChoice == '1':
        meadow(hero)
    elif myChoice == '2':
        forest(hero)


def meadow(hero):
    filename = (path + "/meadow.txt")
    myChoice = story.read(filename, 2, hero)
    if myChoice == '1':
        picnic(hero)
    elif myChoice == '2':
        forest(hero)

def forest(hero):
    filename = (path + "/forest.txt")
    myChoice = story.read(filename, 2, hero)
    if myChoice == '1':
        lightstove(hero)
    elif myChoice == '2':
        meadow(hero)

def picnic(hero):
    story.read(path + "/eat_picnic.txt", None, hero)


def lightstove(hero):
    story.read(path + 'light_stove.txt', None, hero)

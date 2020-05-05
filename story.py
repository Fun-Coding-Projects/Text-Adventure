#!/usr/bin/env python3.8

import time
import os
import path
from world import hero


def main():
    title()
    clear()
    begin()


def title():
    clear()
    f = open('title.txt')
    for line in f:
        print(line, end='')
        time.sleep(0.1)
    input(f'\n{"Press ENTER to continue!":^80}')


def begin():
    name = read('01-Start.txt', None, None)
    hero['name'] = name.title().strip()
    mychoice = read('02-path.txt', 2, hero)
    if mychoice == '1':
        path.Arcane(hero)
    elif mychoice == '2':
        path.Warrior(hero)
    else :
        print(mychoice)
        time.sleep(5)
        begin()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def read(filename, options, hero):
    clear()
    f = open(filename, 'r', newline=None)
    text = f.read()
    if hero:
        for k in hero:
            text = text.replace('{' + k + '}', hero[k])
    responce = input(text)
    if options:
        choice = choose(responce, options)
        return choice
    return responce
    f.close()


def choose(responce, options):
    while True:
        if int(responce) > 0 and int(responce) <= options:
            break
        elif responce == 'help' or 'h':
            print('Please enter a number or type "quit" to exit.')
            # return read(responce, options)
        elif responce == 'quit' or 'q':
            quit()
        else :
            print('Error')
            time.sleep(3)
            continue
    return responce  


if __name__ == '__main__':
    main()

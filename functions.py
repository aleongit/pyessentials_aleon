# -*- coding: utf-8 -*-
# Aleix Leon

import os
from constants import *

# funcions ______________________________________________


def printCategories():
    print()
    for index, cat in enumerate(CATEGORIES):
        print(f"{index + 1}. {cat}")
    print()


def indexCategories():
    return [str(index + 1) for index, el in enumerate(CATEGORIES)]


def printExercicisCategoria(index):
    cat = CATEGORIES[index]
    print()
    print('='*50)
    print(f"{cat.upper()}")
    print('='*50)
    print()

    for k, v in ESSENTIALS.items():
        if cat == v['category']:
            print(f"{k}. {v['title']}")
    print()


def indexExercicisCategoria(index):
    cat = CATEGORIES[index]
    return [k for k, v in ESSENTIALS.items() if cat == v['category']]


def runExercici(num):
    print(f"{num}. {ESSENTIALS[num]['text']}")

    command = f"python {ESSENTIALS[num]['script']}"

    # si arguments
    if 'arguments' in ESSENTIALS[num]:
        if ESSENTIALS[num]['arguments']:
            print('Introdueix arguments: ')
            arg = input(command + ' ')
            os.system(f"{command} {arg}")
    else:
        os.system(f"{command}")
    input('\nPrem una tecla ...')

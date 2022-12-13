# -*- coding: utf-8 -*-
# Aleix Leon

import os
from constants import *

# funcions ______________________________________________

def printMenu():
    print()
    cat = None
    for k, v in ESSENTIALS.items():
        if cat != v['category']:
            cat = v['category']
            print(f"\n{v['category'].upper()}")
            print('='*50)
        print(f"{k}. {v['title']}")
    print()


def runExercici(num):
    print(f"{num}. {ESSENTIALS[num]['text']}")
    os.system(f"python {ESSENTIALS[num]['script']}")
    input('\nPrem una tecla ...')

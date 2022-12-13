# -*- coding: utf-8 -*-
# Aleix Leon

# imports ______________________________________________
#import os

# constants ______________________________________________
from constants import *

# classes objecte ______________________________________________

# funcions ______________________________________________
from functions import *

# test ______________________________________________________________
#command = 'python py/11.py'
#print(ESSENTIALS.keys())
#print('' in ESSENTIALS.keys())

# programa ______________________________________________________________
if __name__ == "__main__":
    
    # init
    opcat = None

    while opcat != '0':
        printCategories()
        print(indexCategories(), end=' ')
        print('[0 Sortir]')
        opcat = input("Opció: ")
        if opcat in indexCategories():
            op = None
            while op != '0':
                printExercicisCategoria(int(opcat)-1)
                print(indexExercicisCategoria(int(opcat)-1), end=' ')
                print('[0 <<]')
                op = input("Opció: ")
                if op in ESSENTIALS.keys():
                    runExercici(op)

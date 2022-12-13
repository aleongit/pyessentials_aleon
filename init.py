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
    op = None

    while op != '0':
        printMenu()
        op = input("Opció [0 Sortir]: ")
        #print(op)
        if op in ESSENTIALS.keys():
            runExercici(op)

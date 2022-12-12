# -*- coding: utf-8 -*-
# Aleix Leon

# imports ______________________________________________
import os

# constants ______________________________________________
from constants import *

# classes objecte ______________________________________________

# funcions ______________________________________________

# test ______________________________________________________________
command = 'python py/11.py'
op = None

print(ESSENTIALS.keys())
print('' in ESSENTIALS.keys())

while op != '0':
    for k,v in ESSENTIALS.items():
        print(v['title'])
    op = input("opció: ")
    print(op)
    if op in ESSENTIALS.keys():
        print
        #os.system(f'python py/{op}.py')
        os.system(f"python {ESSENTIALS[op]['script']}")

# programa ______________________________________________________________
if __name__ == "__main__":
    # inicialtzem
    pass

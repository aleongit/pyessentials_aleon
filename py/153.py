#Aleix Leon

#Exercicis d’argument per línia de comandes

#3
# programa que generi una llista formada per tots els paràmetres que li passem com argument
# i la mostri per consola.

from module15 import *

#control número arguments
if  arg() == 0:
    print("Cap argument")
else:
    #generem llista arguments passats
    ll = [el for el in sys.argv]
    
    #mostrar per consola a partir pos 1 (0 és nom fitxer)
    for i in range(1,len(sys.argv)):
        print(f"Arg {i}: {sys.argv[i]}")
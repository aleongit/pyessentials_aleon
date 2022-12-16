#Aleix Leon

#Exercicis d’argument per línia de comandes

#5
# programa que accepta una data com a argument, en format dd/mm/aaaa,
# comprova que el format és correcte i ens retorna a quin dia de la setmana correspon.
# Podeu fer servir la biblioteca datetime.

from module15 import *

#control número arguments
if  arg() == 1:
    
    #paràmetre data
    d = sys.argv[1]
    
    #funció data retorn dia o None
    print(f"{d} dia setmana:",dia_dma(d))    
    
else:
    print("Nº d'arguments incorrectes")
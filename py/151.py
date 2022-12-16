#Aleix Leon

#Exercicis d’argument per línia de comandes

#1
#Programa que accepta 1 argument per la línia de comandes
#i si està format per lletres mostra per pantalla quantes vocals té.

from module15 import *

# nombre d'arguments
n = len(sys.argv)
print("Nombre d'arguments passats:", n-1)
print()

#control només 1 argument (nom programa + 1r arg)
if arg() == 1:
    cadena = sys.argv[1]
    #l'argument sempre serà tipus string
    #suposem cadena només lletres
    
    #depurem accents si n'hi ha
    cadena = treu_accents(cadena)
    #print(nomes_lletres(cadena))
    if not nomes_lletres(cadena):
        print("La cadena no està formada només per lletres")
    else:
        print("OK cadena de lletres\n")
        print(conta_vocal(cadena.lower()))
        print(f"\n{conta_vocals(cadena.lower())} vocals totals")

else:
    print("Cal 1 argument\n")
    # Arguments passats
    print("Arguments passats:")
    for i in range(n):
        print(i,"...",sys.argv[i])
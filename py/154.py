#Aleix Leon

#Exercicis d’argument per línia de comandes

#4
# Fes un programa que comprovi que el nombre d’arguments és superior a 1,
# que són alfabètics i en aquest cas que els ordeni alfabèticament.
# Sinó que mostri quin error hi ha.

from module15 import *

ll_errors = []

#control número arguments
if  arg() > 1:
    
    #control arguments alfabètics
    #suposem només lletres
    
    #copiem llista
    a = sys.argv.copy()
    
    #el 1r arg molesta, traiem
    a.pop(0)
    
    ll_errors = tots_lletres(a)
    
    #si llista és buida
    if len(ll_errors) == 0:
        a.sort()
        print(*a, sep="\n")
    else:
        for i in range(len(ll_errors)):
            print(f"*ERROR Arg) {ll_errors[i]} \t>> No alfabètic")
else:
    print("Mínim 2 arguments")
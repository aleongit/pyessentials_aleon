#Aleix Leon

#3-1
#Crea un fitxer de text saluda.txt, amb python amb el contingut:
#"Bon dia CLASSE!!".  i tanca'l.
#Obre el fitxer anterior, i afegeix-li les següents frases, cadascuna en una línia diferent: 
#Bona nit a tot@s !!!
#Buff no puc dormir, potser que compti xaiets


fitxer ="saluda.txt"
l1 = "Bon dia CLASSE!!"
l2 = "Bona nit a tot@s !!!"
l3 = "Buff no puc dormir, potser que compti xaiets"

def printFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

try:
    #obrim fitxer w i tanquem
    with open(fitxer, "w", encoding="utf8") as f:
     #escrivim línies a fitxer
        f.write(l1 + "\n")
    printFitxer(fitxer)
    
    #tornem a obrim fitxer a i tanquem
    with open(fitxer, "a", encoding="utf8") as f:
     #escrivim línies a fitxer
        f.write(l2 + "\n") + f.write(l3)
    printFitxer(fitxer)

#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass



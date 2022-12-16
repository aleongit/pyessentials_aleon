#Aleix Leon

#2-1
#Fes programa que llegeixi del fitxer "text.txt"
#i escrigui les línies parells en un fitxer nou de nom "text3.txt".
#Mostra en el mateix programa el contingut del fitxer "text3.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).

fitxer1 ="text.txt"
fitxer2 ="text3.txt"

def printFitxer(fitxer):
    print(fitxer)
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

try:
    #obrim fitxers r + w
    with open(fitxer1, "r", encoding="utf8") as f1:
        with open(fitxer2, "w", encoding="utf8") as f2:
            printFitxer(fitxer1)
            #llegim línies fitxer a llista
            linies = f1.readlines()[::2]
            #print(linies)
            #escrivim línies a fitxer
            for l in linies:
                f2.writelines(l)
    printFitxer(fitxer2)

#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass



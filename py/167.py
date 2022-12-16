#Aleix Leon

#2-2
#Fes un programa que llegeixi del fitxer "text.txt",
#afegeixi un punt a totes les línies del fitxer "text.txt"
#i les escrigui en un fitxer nou de nom "text4.txt".
#Mostra en el mateix programa el contingut del fitxer "text4.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).


fitxer1 ="text.txt"
fitxer2 ="text4.txt"

def printFitxer(fitxer):
    print(fitxer)
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

# agafem fins abans intro, posem punt i intro
def puntLinia(ll):
    return [str(el)[:-1] + ".\n" for el in ll]

try:
    #obrim fitxers r + w
    with open(fitxer1, "r", encoding="utf8") as f1:
        with open(fitxer2, "w", encoding="utf8") as f2:
            printFitxer(fitxer1)
            #llegim línies fitxer a llista
            linies = f1.readlines()
            linies = puntLinia(linies)
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



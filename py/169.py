#Aleix Leon

#2-4
#Fes un programa que llegeixi del fitxer "text2.txt"
#i escrigui en un fitxer nou de nom "text6.txt" només les línies parells.
#Després llegeixi del fitxer "text3.txt"
#i escrigui a continuació en el fitxer "text6.txt" només les línies senars.
#Mostra en el mateix programa el contingut del fitxer "text6.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).

fitxer1 ="text2.txt"
fitxer2 ="text3.txt"
fitxer3 ="text6.txt"

def printFitxer(fitxer):
    print(fitxer)
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

try:
    #obrim fitxers r + w + r
    with open(fitxer1, "r", encoding="utf8") as f1:
        with open(fitxer2, "r", encoding="utf8") as f2:
            with open(fitxer3, "w", encoding="utf8") as f3:
                printFitxer(fitxer1)
                printFitxer(fitxer2)
                #llegim línies dels dos fitxers oberts
                linies = f1.readlines()[::2] + f2.readlines()[1::2]
                #escrivim línies a fitxer
                for l in linies:
                    f3.writelines(l)
                
    printFitxer(fitxer3)

#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass



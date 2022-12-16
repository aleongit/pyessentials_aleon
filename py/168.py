#Aleix Leon

#2-3
#Fes un programa que llegeixi del fitxer "text2.txt"
#i l'escrigui en un fitxer nou de nom "text5.txt".
#Després llegeixi del fitxer "text3.txt" i l'escrigui a continuació en el fitxer "text5.txt"
#(hi haurà tot el contingut del fitxer "text2.txt" i després tot el contingut del fitxer "text3.txt").
#Mostra en el mateix programa el contingut del fitxer "text5.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).


fitxer1 ="text2.txt"
fitxer2 ="text3.txt"
fitxer3 ="text5.txt"

def printFitxer(fitxer):
    print(fitxer)
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

try:
    #obrim fitxers r + r + w
    with open(fitxer1, "r", encoding="utf8") as f1:
        with open(fitxer2, "r", encoding="utf8") as f2:
            with open(fitxer3, "w", encoding="utf8") as f3:
                printFitxer(fitxer1)
                printFitxer(fitxer2)
                #llegim línies dels dos fitxers oberts
                linies = f1.readlines() + f2.readlines()
                #escrivim línies a fitxer
                for l in linies:
                    f3.writelines(l)
                
    printFitxer(fitxer3)

#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass



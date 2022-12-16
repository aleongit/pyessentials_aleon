#Aleix Leon

#5
#Fes un programa que llegeixi del fitxer "text.txt"
#i escrigui el contingut en un fitxer nou de nom "text2.txt".
#Mostra en el mateix programa el contingut del fitxer "text2.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).

fitxer1 ="text.txt"
fitxer2 ="text2.txt"

def printFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())
    
#1 obrim fitxers 1 mode lectura, 2 escriptura
with open(fitxer1, "r", encoding="utf8") as f1:
    with open(fitxer2, "w", encoding="utf8") as f2:
        print("Fitxer1:")
        printFitxer(fitxer1)
        #llegim línies fitxer a llista
        linies = f1.readlines()
        #print(linies)
        #escrivim línies a fitxer
        for l in linies:
            f2.writelines(l)

print("Fitxer2:")
printFitxer(fitxer2)

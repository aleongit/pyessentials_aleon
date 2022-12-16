#Aleix Leon

#4
#Modifica els 3 programes anterior usant la comanda with i no fent servir la comanda close.
#Posa tot el codi en un sol programa.

linies = ["línia1\n","línia2\n","línia3\n"]
linia = "Línia nova\n"
fitxer ="text.txt"

def printFitxer():
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())
    
#1 obrim fitxer mode escriure
with open(fitxer, "w", encoding="utf8") as f:
    #escrivim línies a fitxer
    for l in linies:
        f.writelines(l)

#2 obrim fitxer mode lectura
printFitxer()
    
#3 obrim fitxer mode append
with open(fitxer, "a", encoding="utf8") as f:
    #afegim línia
    f.writelines(linia)

printFitxer()
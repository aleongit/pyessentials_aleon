#Aleix Leon

#2-5
#Fes un programa que llegeixi del fitxer "text2.txt" i del fitxer "text3.txt"
#i escrigui en un fitxer nou de nom "text7.txt" alternadament línies d'un fitxer i de l'altre
#(compte: els 2 fitxers no tenen el matexi nombre de línies, un s'acabarà abans que l'altre).
#Mostra en el mateix programa el contingut del fitxer "text7.txt"
#(l'hauràs de tornar a obrir ara en mode lectura).


fitxer1 ="text2.txt"
fitxer2 ="text3.txt"
fitxer3 ="text7.txt"

def printFitxer(fitxer):
    print(fitxer)
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())
        
def alternaLinies(ll1,ll2):
    #miro la llista mes curta
    minima = min(len(ll1),len(ll2))
    ll = []
    #alterno elements traient 1a pos
    for i in range(minima):
        ll.append(ll1.pop(0))
        ll.append(ll2.pop(0))
    #extenc la resta elements de la llista no buida
    if len(ll1) == 0:
        ll.extend(ll2)
    else:
        ll.extend(ll1)
    return ll

try:
    #obrim fitxers r + w + r
    with open(fitxer1, "r", encoding="utf8") as f1:
        with open(fitxer2, "r", encoding="utf8") as f2:
            with open(fitxer3, "w", encoding="utf8") as f3:
                printFitxer(fitxer1)
                printFitxer(fitxer2)
                #llegim línies dels dos fitxers oberts
                linies = f1.readlines()
                linies2 = f2.readlines()
                lfinals = alternaLinies(linies,linies2)
                #escrivim línies a fitxer
                for l in lfinals:
                    f3.writelines(l)
                
    printFitxer(fitxer3)

#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass



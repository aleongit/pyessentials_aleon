#Aleix Leon

#3-3
#Castiga a Python a escriure en un fitxer castiga.txt: 
#1. Faré totes les tasques de python perquè vull aprovar
#2. Faré totes les tasques de python perquè m’agrada programar
#3. Faré totes les tasques de python perquè vull aprovar
#2. Faré totes les tasques de python perquè m’agrada programar
#... 
#1000. Faré totes les tasques de python perquè m’agrada programar

#Utilitza una funció:
#escriu_castig(cadena_castig1, cadena_castig2, vegades_q_escriu) 

fitxer = "castiga.txt"
castig1 = "Faré totes les tasques de python perquè vull aprovar\n"
castig2 = "Faré totes les tasques de python perquè m’agrada programar\n"

def printFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

#retorno cadena resultant d'una llista
#alterno línies depenent si l'índex és parell o senar
def escriu_castig(c1,c2,n):
    return "".join([str(i+1)+".\t"+c1 if i % 2 == 0 else str(i+1)+".\t"+c2 for i in range(n)])

try:
    #obrim fitxer w i tanquem
    with open(fitxer, "w", encoding="utf8") as f:
        #escri cadena a fitxer
        f.write(escriu_castig(castig1,castig2,1000))
    printFitxer(fitxer)
    
#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass


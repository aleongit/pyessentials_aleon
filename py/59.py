#Aleix Leon

#Programa l’algorisme del xifratge del Cèsar.
#Fes dues versions en Python: amb llistes i amb cadenes.
#Prova'l amb la frase "m'agraden els algorismes classics".
# -----------------------------------------------------------------------

#declaració
import string
ABC = string.ascii_lowercase #abecedari 'az'
ABCX = ""
#D = 3 #desplaçament
missatge = "m'agraden els algorismes classics"
missatgeX = ""
versions = ["Versió Cadenes","Versió Llistes"]
opcions = ""
MIDA = len(ABC)

print("Algorismes Clàssics: Xifratge del Cèsar")

#preguntem a usuari opció
opcio = 0
while (opcio < 1) or (opcio > len(versions)):
    #mostro a usuari opcions i (posició + 1)
    for i in range(len(versions)):
        print("[Opció " + str(i + 1) + "]", versions[i])
        opcions += "[" + str(i + 1) + "]"
    #demano opció
    opcio = int( input("\nQuina versió triem " + opcions + " ? "))
    opcions = ""

v = versions[opcio-1]
#copio valor triat

#XIVATO
print()
print(v)

#preguntem desplaçament, i que no serà més gran que 'mida'
d = -1
while (d < 0) or (d > MIDA):
    d = int( input("Quin desplaçament hi posem ? [0-" + str(MIDA) + "]: "))

#Versió Cadenes
if opcio == 1:
    #per cada lletra abc, calculem posició desplaçada
    #que serà el residu de (posició + desplaçament) / mida
    #així quan l'índex arribi a 26 o més gran, tornem a les posicions inicials
    #(i+d) fins a mida 26 serà residu (i+d)     3%26 = 3 ... 25%26 = 25
    #(i+d) quan sigui 26 serà residu 0                       26%26 = 0
    #(i+d) quan sigui 27 serà residu 1                       27%26 = 1
    #(i+d) quan sigui 28 serà residu 2 ...                   28%26 = 2
    for i in range(MIDA):
        #la lletra codificada és el residu de (posició 'i' + desplaçament) / mida
        ABCX += ABC[(i+d)%MIDA]
        #print(i+d,(i+d)%MIDA)
    print("\nABC :", ABC)        
    print("ABCX:", ABCX)

    #codifiquem missatge
    #per cada lletra del missatge
    #si la lletra està en ABC, busca la posicio d'on està en ABC, i posa-hi la lletra de ABCX de la mateixa posició
    #si la lletra no està (un espai, un símbol) deixa-ho igual
    for lletra in missatge:
        if lletra in ABC:
             missatgeX += ABCX[ABC.index(lletra)]
        else:
             missatgeX += lletra

#Versió Llistes
elif opcio == 2:
    
    #declaro
    llABC = list(ABC) #genero llista de l'abecedari
    llABCX = []
    MIDA = len(llABC) #la mida de llista i string és la mateixa, però ho canvio per recalcar
    
    #creo llista abc codificada per llista utilitzant algorisme anterior strings
    #no veig millor manera de fer-ho
    for i in range(MIDA):
        llABCX.append(llABC[(i+d)%MIDA])
    
    print("\nLLISTA ABC :", llABC)        
    print("LLISTA ABCX:", llABCX)
    
    #codifico missatge també amb algorisme anterior strings
    #no veig millor manera de fer-ho
    for lletra in missatge:
        if lletra in llABC:
            missatgeX += llABCX[ABC.index(lletra)]
        else:
            missatgeX += lletra
print()
print(missatge)
print(missatgeX)
    

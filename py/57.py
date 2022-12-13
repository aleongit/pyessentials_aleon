#Aleix Leon

#Programa l’algorisme dEuclides (les dues versions). Prova’l amb 1071 i 462.
#Per MCD (=màxim comú divisor)
# -----------------------------------------------------------------------

#declaració
A = 1071
B = 462

versions =["Residu","Resta"]
opcions = ""

print("Algorismes Clàssics: Algorisme d’Euclides")

#vull preguntar quina versió utilitzarem mitjançant llista flexible d'opcions
#m'hi he posat i per fer-ho maco (podria servir com a menú)
#no era necessari, però m'ha fet pena borrar-ho..

#controlo opció amb un 'mentre' per acotar posicions vàlides
opcio = 0
while (opcio < 1) or (opcio > len(versions)):
    #mostro a usuari opcions i (posició + 1)
    #si hi hagués més opcions tindria més sentit
    for i in range(len(versions)):
        print("[Opció " + str(i + 1) + "]", versions[i])
        opcions += "[" + str(i + 1) + "]"
        opcions = ""
    #demano opció
    opcio = int( input("\nQuina versió triem " + opcions + " ? "))

v = versions[opcio-1]
#copio valor triat

#XIVATO
print("Versió", v)

#apliquem algorisme d'Euclides segons versió
#inicialitzem variables
dend = A
dsor = B
temp = 0

if v == "Residu":
    while dsor != 0:
        #print("Xivato:", dsor)
        temp = dsor
        dsor = dend % dsor
        dend = temp

elif v == "Resta":
    while dsor != 0:
        if dend > dsor:
            dend = dend - dsor
        else:
            dsor = dsor - dend
            #print("Xivato:", dsor)

print("El MCD de", A ,"i de", B ,"és", dend)


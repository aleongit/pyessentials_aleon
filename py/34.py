#Aleix Leon

#mostra la suma i multiplicació de tots els elements d'una llista.
#introduir la llista per teclat.
#Ajuda: feu servir un bucle per afegir elements a la llista. 

#definim llista buida
llista = []

#inicialitzo acumuladors
suma = 0
mult = 1

#demanem mida
mida = int (input("Quina mida vols per la llista: "))

#bucle per recorre llista per index (de 0 a mida)
for i in range(mida):
    #demano num per cada posició
    num = int (input("Introdueix enter per posició " + str(i) + " de la llista: "))
    #afageixo el num al final de la llista
    llista.append(num) #o llista += [num]
    
    #aprofito el bucle per sumar i multiplicar
    suma = suma + num
    mult = mult * num

print("La llista de valors és:", llista)
print("La suma d'aquests valors és:", suma)
print("La multiplicació d'aquests valors és:", mult)

#Aleix Leon

#obtenir el nombre més gran, més petit i la mitjana d'una llista de sencers.
#introduir la llista per teclat.
#Fer versió bucle i versió mètodes.
#Ajuda: feu servir un bucle per afegir elements a la llista.

#definim llista buida
llista = []

#inicialitzo
maxim = 0
minim = 0
acum = 0

#demanem mida
mida = int (input("Quina mida vols per la llista: "))

#bucle per crear la llista per index (de 0 a mida)
for i in range(mida):
    #demano num per cada posició
    num = int (input("Introdueix enter per posició " + str(i) + " de la llista: "))
    #afageixo el num al final de la llista
    llista.append(num) #o llista += [num]
    
    #aprofito el bucle per max, min i mitja
    
    #acumulo per mitjana
    acum = acum + llista[i]
    
    #el 1r element serà max i min
    if i == 0:
        maxim = llista[i]
        minim = llista[i]
    #comparo els següents elements de la llista per si hi ha un nou max i min
    else:
        if llista[i] > maxim:
            maxim = llista[i]
        if llista[i] < minim:
            minim = llista[i]
        
print("La llista de valors és:", llista)
print("El nombre més gran per 'versió bucle' és:", maxim)
print("El nombre més petit per 'versió bucle' és:", minim)
print("La mitjana dels valors per 'versió bucle' és:", acum/mida)
print("")
print("El nombre més gran per 'versió mètode' és:", max(llista))
print("El nombre més petit per 'versió mètode' és:", min(llista))
print("La mitjana dels valors per 'versió mètode' és:", sum(llista)/mida)

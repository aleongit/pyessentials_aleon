#Aleix Leon

#Programa l’algorisme d’ordenació de la bombolla. Prova’l amb L1 i L2.
# L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# L2 = [12, 1, 12, 1, 8, 5, 1, 3]
# -----------------------------------------------------------------------

#declaració
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
ll = []
opcions = [L1,L2] #llista de llistes per opcions (by Pilar)

print("Algorismes Clàssics: Ordenació de la bombolla")

#vull preguntar quina llista ordenar, si L1 o L2
opcio = 0
while opcio !=1 and opcio != 2:
    opcio = int( input("Quina llista ordenem L[1] o L[2]: "))

ll = opcions[opcio-1].copy()
#copiem la llista corresponent (per posició) de la llista d'opcions (by Pilar)

print(ll)

#ordenem de la bombolla

n = len(ll) #agafem mida
intercanvi = True #boleana per saber si o no intercanvi

while intercanvi: #mentre hi hagi 'intercanvi'
    intercanvi = False #inicialitzem
    
    for i in range(1, n): #valors de 1 a mida
        #print(i)
        if ll[i-1] > ll[i]:
            #intercanvi de pos actual amb anterior
            aux = ll[i]
            ll[i] = ll[i-1]
            ll[i-1] = aux
            
            intercanvi = True
    n -= 1 #reduim 1 posició cada vegada perquè els valors que deixem a la dreta són els més grans

print(ll)
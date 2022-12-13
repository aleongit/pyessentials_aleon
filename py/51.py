#Aleix Leon

# Programa l’algorisme d’ordenació per inserció. Prova’l amb L1 i L2.
# L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# L2 = [12, 1, 12, 1, 8, 5, 1, 3]
# -----------------------------------------------------------------------

#declaració
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
ll = []
opcions = [L1,L2] #llista de llistes per opcions (by Pilar)

print("Algorismes Clàssics: Ordenació per inserció")

#vull preguntar quina llista ordenar, si L1 o L2
opcio = 0
while opcio !=1 and opcio != 2: #while per assegurar les opcions
    opcio = int( input("Quina llista ordenem L[1] o L[2]: "))

ll = opcions[opcio-1].copy()
#copiem la llista corresponent (per posició) de la llista d'opcions (by Pilar)

print(ll)

#ordenem per inserció
i = 1
while i < len(ll):
    x = ll[i] # copiem valor a 'x', que és el valor a insertar
    j = i - 1
    
    while (j >=0) and ll[j] > x: #anirem movent valors cap amunt (fent lloc)
        ll[j+1] = ll[j] # fem lloc per la 'x', pujant el valor cap a la dreta
        j = j - 1
    
    ll[j+1] = x # aquí insertem la 'x'
    i = i + 1
    
print(ll)
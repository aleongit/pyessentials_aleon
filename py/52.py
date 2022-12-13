#Aleix Leon

#Programa l’algorisme d’ordenació del nan. Prova’l amb L1 i L2.
# L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# L2 = [12, 1, 12, 1, 8, 5, 1, 3]
# -----------------------------------------------------------------------

#declaració
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
ll = []
opcions = [L1,L2] #llista de llistes per opcions (by Pilar)

print("Algorismes Clàssics: Ordenació del nan")

#vull preguntar quina llista ordenar, si L1 o L2
opcio = 0
while opcio !=1 and opcio != 2:
    opcio = int( input("Quina llista ordenem L[1] o L[2]: "))

ll = opcions[opcio-1].copy()
#copiem la llista corresponent (per posició) de la llista d'opcions (by Pilar)

print(ll)

#ordenem per nan
pos = 0
while pos < len(ll): #fins que no arribem al final de llista
    
    #si està al principi o la posició és més gran que l'anterior, continua amb la llista
    if (pos == 0) or ll[pos] >= ll[pos-1]:
        pos += 1 #incrementem posició
    
    #si la posició anterior és mes gran que la actual, tire enrrere la posició actual
    else:
        #intercanviem posició amb posició anterior
        guarda = ll[pos]
        ll[pos] = ll[pos-1]
        ll[pos-1] = guarda
        
        pos -= 1 #decrementem posició, tornem enrere
        
print(ll)
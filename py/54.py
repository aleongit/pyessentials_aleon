#Aleix Leon

#Programa l’algorisme de cerca seqüencial. Prova’l amb L1 i L2.
# L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# L2 = [12, 1, 12, 1, 8, 5, 1, 3]
# -----------------------------------------------------------------------

#declaració
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
ll = []
opcions = [L1,L2] #llista de llistes per opcions (by Pilar)

print("Algorismes Clàssics: Cerca seqüencial")

#vull preguntar quina llista utilitzem, si L1 o L2
opcio = 0
while opcio !=1 and opcio != 2:
    opcio = int( input("Quina llista utilitzem ? L[1] o L[2]: "))

ll = opcions[opcio-1].copy()
#copiem la llista corresponent (per posició) de la llista d'opcions (by Pilar)

#XIVATO
print(ll)

#preguntar element a cercar
el = int( input("Valor a cercar ? "))

#apliquem algorisme cerca seqüencial, començant per la 1a posició (0)
i = 0
#recorre la llista fins el final i mentre no es trobi element
while (i < len(ll)) and (el != ll[i]):
    #incrementem posició
    i += 1

#si s'ha arribat al final, no s'ha trobat
if i == len(ll):
    print(el , "No trobat")
#si es troba, surt del bucle i es mostra posició
else:
    print(el , "Trobat a la posició", i)
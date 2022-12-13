#Aleix Leon

#Programa l’algorisme de cerca seqüencial amb llista ordenada. Prova’l amb L3.
# L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]
# -----------------------------------------------------------------------

#declaració
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17] #LLISTA ORDENADA
ll = []

ll = L3.copy()
#copio llista per treballar

#XIVATO
print(ll)

#preguntar element a cercar
el = int( input("Valor a cercar ? "))

#apliquem algorisme cerca seqüencial ORDENADA, començant per la 1a posició (0)
i = 0
#recorre la llista fins el final i mentre element sigui més gran que el valor de la llista
while (i < len(ll)) and (el > ll[i]):
    #incrementem posició
    i += 1

#no es troba, si s'ha arribat al final o si s'ha sortit del bucle però no coincideix l'element amb valor de posició
if (i == len(ll)) or (el != ll[i]):
    print(el , "No trobat")
#trobat, si es surt i coincideix element amb valor posició
else:
    print(el , "Trobat a la posició", i)
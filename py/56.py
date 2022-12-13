#Aleix Leon

#Programa l’algorisme de cerca binària. Prova’l amb L3 i un valor entrat per teclat.
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

#apliquem algorisme cerca binària
#inicialitzem variables
trobat = False
inf = 0             #límit inferior la 1a posició
sup = len(ll) - 1   #límit superior serà la longitud de la llista (-1 posició) sinó peta

#fer mentre límit inferior s'apropi o sigui igual a inferior, i no es trobi valor
while (inf <= sup) and (not trobat):
    #busca posició mig, que serà la meitat dels dos límits + la posició inferior anterior
    mig = (sup - inf) // 2 + inf
    #print("...mig a pos", mig)
    #si l'element és igual al valor acotat del mig ,trobat
    if el == ll[mig]:
       trobat = True
    else:
       if el < ll[mig]:
         sup = mig - 1 #decrementem nivell superior
         #print("...inf-sup", inf,"-", sup)
       else:
         inf = mig + 1 #incrementem nivell inferior
         #print("...inf-sup", inf,"-", sup)

if not trobat:
    print(el , "No trobat")
else:
    print(el , "Trobat a la posició", mig)
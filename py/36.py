#Aleix Leon

#donada una llista strings, comptar quants strings de longitud >= 2 i comencen per 'A'
#mostrar per pantalla el resultat
#exemple : llista =  ['abc', 'xyz', 'aba', '1221', 'a']

#definim llista buida
ll = []

#inicialitzem
conta = 0

#demanem mida
mida = int (input("Quina mida vols per la llista: "))

#bucle per recorre llista per index (de 0 a mida)
for i in range(mida):
    #demano string per cada posició
    frase = input("Introdueix string per posició " + str(i) + " de la llista: ")
    #afageixo al final de la llista
    ll.append(frase)
    
    #print(len(ll[i]))
    #print(len(ll[i][0]))
    
    #miro 2 condicions: longitud i si la 1a pos comença per 'A'
    if (len(ll[i]) >= 2) and (ll[i][0].upper() == 'A'):
        #si ho compleix, comptador
        conta += 1

print("La llista de valors és:", ll)
print("Tenim ", conta, "strings de longitud >= 2 i que comencen per 'A'")

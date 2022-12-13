#Aleix Leon

#eliminar duplicats d'una llista.  
#exemple : llista =  [1,2,3,1,3,1,4,2], sortida = [1,2,3,4]

#definim llistes buides
ll = []
ll_final = []

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
    
#recorro per cada element de llista ll
for element in ll:
    #si l'element no està a la nova llista, afageix
    #d'aquesta manera no afegirà element si ja hi és i evitem els repetits
    if element not in ll_final:
        ll_final.append(element)
        
print("Llista inicial:", ll)
print("Llista sense repetits:", ll_final)

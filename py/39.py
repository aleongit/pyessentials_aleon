#Aleix Leon

#imprimir els números d'una llista especificada per teclat
#després d'eliminar-ne els números parells.

#definim llistes buides
ll = []
ll_final = []

#demanem mida
mida = int (input("Quina mida vols per la llista: "))

#bucle per recorre llista per index (de 0 a mida)
for i in range(mida):
    #demano string per cada posició
    n = int (input("Número enter per posició " + str(i) + " de la llista: "))
    #afageixo al final de la llista
    ll.append(n)

#demanar element a eliminar
print("Llista introduïda:", ll)

#recorro per cada element de llista ll
for n in ll:
#afageixo a nova llista els que no són parells
    if not (n % 2 == 0):
        ll_final.append(n)

print("Llista sense parells:", ll_final)

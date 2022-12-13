#Aleix Leon

#sumar un valor per teclat a tots els elements de la llista [1,2,3,4,5,6,7,8,9,10]
#utilitzar bucle for per modificar la llista original.

#definim llista de valors
llista = [1,2,3,4,5,6,7,8,9,10]

valor = int(input("Introdueix valor: "))

#faig copia per si de cas, treballaré amb còpia
ll = llista.copy()

#bucle for on recorro per index cada element de la llista
for i in range(len(ll)):
    #print(i, ll[i])
    ll[i] += valor
    
print ("Llista Original: ", llista)
print ("+ ", valor)
print ("Llista Final   : ", ll)

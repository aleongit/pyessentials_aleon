#Aleix Leon

#comprovar si dues llistes tenen elements en comú
#llista1 = [1,2,3,4,5,6,7]
#llista2 = [4,1,20,100]
#imprimeix per pantalla 'Té 2 elements en comú i són: 1,4'

#definim llistes a comparar
llista1 = [1,2,3,4,5,6,7]
llista2 = [4,1,20,100]
#llista2 = [1,2,3,4,5,6,7]

#llista resultat buida
ll_final =[]

#recorro per cada element de llista llista 1 i després per cada de llista 2
for v1 in llista1:
    for v2 in llista2:
        #si troba un valor comú, l'afageixo a nova llista resultat
        if v1 == v2:
            ll_final.append(v1)

print("Té 2 elements en comú i són:", ll_final)

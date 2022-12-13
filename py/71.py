#Aleix Leon

#Tuples
#11 exercicis amb menú

# 1. Crear una tupla nova que sigui la tupla girada (al revés)
# aTuple = (10, 20, 30, 40, 50)

# 2. Crar una tupla d’un sol element anomenada unSol i amb contingut 50

# 3. Fer un swap de les següents tuples 2 versions, amb variable auxiliar i directament
# tuple1 = (99, 88)
# tuple2 = (11, 22)

# 4. Ordena la tupla pel segon element: algorismes treballats (bombolla, nan o inserció)
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#sortida esperada (('c', 11), ('a', 23), ('d', 29), ('b', 37))

# 5. Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?
# tuple1 = (50, 10, 60, 70, 50)

# 6. Comprova si tots els ítems de la tupla tenen el mateix valor
# tuple1 = (45, 45, 45, 45)

# 7. Com es crea una tupla buida? Com es converteix una tupla en una llista?
# 
# 8. Tenint una llista de números, crear una llista de tuples amb el 1r element com a número i el 2n com a cub del número.
# 
# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# 9. Fes una llista de tuples de totes les combinacions possibles de 2 tuples d'arguments. 
# Input : t1 = (7, 2), t2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

# 10. Trobar els elements repetits d’una llista i construir una llista de tuples
# on surti en primer terme l’element i en segon terme quantes vegades apareix.
#     llista = [1,2,3,1,2,1,1]
#     sortida = [(1,4),(2,2),(3,1)]

# 11. Troba en quina posició es troba l’element 20:
# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

# -----------------------------------------------------------------------

#declaració

exercicis =["Sortir",\
            "Crear tupla girada al revés",\
            "Crear tupla 1 element (50)",\
            "Swap entre tuples",\
            "Ordenar tupla pel 2n element",\
            "Contar valor 50 i %",\
            "Comprovar si elements són iguals",\
            "Tupla buida i convertir tupla a llista",\
            "Crear llista tuples amb (num, cub del num)",\
            "Llista combinacions entre valors de 2 tuples",\
            "Crear llista tuples amb (num, contador num)",\
            "Troba posició element 20"]
opcio = 1
#menú opcions amb 0 per sortir
while (opcio != 0):

    print("\nTuples")
    
    #mostro a usuari opcions i (posició + 1)
    for i in range(len(exercicis)):
        print("[Opció " + str(i) + "]", exercicis[i])
    #demano opció
    opcio = int( input("\nQuin exercici vols veure ? [1-11] : "))

    print("\nExercici",opcio)
    
    if opcio == 1:
        aTuple = (10, 20, 30, 40, 50)

        print("Versió Slicing")
        # començant pel final (index -1) fins al principi (index -5) amb pas de -1
        bTuple = aTuple[-1:-(len(aTuple)+1):-1]        
        print(aTuple)
        print(bTuple)
        
        print("\nVersió llista + List Comprehension")
        # passo de tupla a llista
        aLlista = list(aTuple)
        #print(type(aLlista))
        bLlista = [aLlista[i] for i in range(-1,-(len(aLlista)+1),-1)]
        #print(bLlista)
        # passo de llista a tupla
        bTuple = tuple(bLlista)
        print(bTuple)
    
    elif opcio == 2:
        unSol = (50,)
        print ("Creada Tupla unSol de tipus",type(unSol),\
               "i de",len(unSol),"element: ", unSol)
    
    elif opcio == 3:
        
        print("\nVersió auxiliar")
        tuple1 = (99, 88)
        tuple2 = (11, 22)
        print("tuple1",tuple1)
        print("tuple2",tuple2)
        print("- swap! -")       
        tupleAux = tuple1
        tuple1 = tuple2
        tuple2 = tupleAux
        print("tuple1",tuple1)
        print("tuple2",tuple2)
        
        print("\nVersió directe")
        tuple1 = (99, 88)
        tuple2 = (11, 22)
        print("tuple1",tuple1)
        print("tuple2",tuple2)
        print("- swap! -")          
        tuple1,tuple2 = tuple2,tuple1
        print("tuple1",tuple1)
        print("tuple2",tuple2)

    elif opcio == 4:
        tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
        
        #PROVES
        #print(tuple1)
        #print(tuple1[0][1])
        #print(tuple1[1][1])
        #print(tuple1[0])
        #print(tuple1[1])
        
        #converteixo tupla a llista, perquè no em deixa modificar posicions des de tupla
        ll_tuple1 = list(tuple1)
                
        #ordenem bombolla
        mida = len(ll_tuple1)
        intercanvi = True
        while intercanvi: #mentre hi hagi 'intercanvi'
            intercanvi = False
            for i in range(1, mida): #valors de 1 a mida
                #comparo amb el 2n element de la llista [1r][2n]
                if ll_tuple1[i-1][1] > ll_tuple1[i][1]:
                    #intercanvi de pos actual amb anterior en bloc [només un index]
                    aux = ll_tuple1[i]
                    ll_tuple1[i] = ll_tuple1[i-1]
                    ll_tuple1[i-1] = aux
                    intercanvi = True
            mida -= 1 #reduim 1 posició cada vegada perquè els valors que deixem a la dreta són els més grans
        
        #print(ll_tuple1)
        print(tuple1)
        #passo els valors ordenats de llista a la tupla inicial
        tuple1 = tuple(ll_tuple1)
        print(tuple1)
        
    elif opcio == 5:
        VALOR = 50
        tuple1 = (50, 10, 60, 70, 50)
        conta = tuple1.count(VALOR)

        print("El valor",VALOR,"surt",conta,"vegades")
        print("Representa un",(conta/len(tuple1))*100,"%")
        
    elif opcio == 6:
        tuple1 = (45, 45, 45, 45)
        
        #passem a 'set' els valors i que seran únics
        unics = set(tuple1)
        #si només hi ha 1 item, vol dir que tots seran iguals
        if len(unics) == 1:
            print("Tots els items de la tupla tenen el mateix valor")
        else:
            print("Els items de la tupla no tenen el mateix valor")

    elif opcio == 7:
        tupla = ()
        print("Per crear una tupla buida, la definim sense elements")
        print("tupla = ()")
        print("tupla és", type(tupla))
        
        llista = list(tupla)
        print("\nPer convertir una tupla a una llista, fem servir 'list'")
        print("llista = list(tupla)")
        print("llista és", type(llista))

    elif opcio == 8:
        llista = [1, 2, 3]
        #Output: [(1, 1), (2, 8), (3, 27)]
        llTuples = []
        
        #versió list comprehension
        #es crea l'element de la llista com a tupla de dos elements, per cada element de la llista inicial
        llTuples = [(el,el**3) for el in llista]
        
        print(llista)
        print(llTuples)
        print("\nLa llista",type(llTuples),"té")
        for el in llTuples:
            print(el,type(el))
        
    elif opcio == 9:
        t1 = (7, 2)
        t2 = (7, 8)
        #Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2),(8, 7), (8, 2)]
        llTuples = []
         
        print("\nVersió amb 2 fors x 2 fors aniuats per element")
        print("Versió list comprehension")
        
        ll1 = [(el1,el2) for el1 in t1 for el2 in t2]
        ll2 = [(el2,el1) for el2 in t2 for el1 in t1]
        
        llTuples = ll1 + ll2
        
        print(t1)
        print(t2)
        print(llTuples)

    elif opcio == 10:
   
        llista = [1,2,3,1,2,1,1]
        #sortida = [(1,4),(2,2),(3,1)]
        llTuples = []
        
        #filtro valors
        valors = set(llista)
        print(valors)
        
        #for el in valors:
        #    llTuples.append((el,llista.count(el)))
        
        llTuples = [(el, llista.count(el)) for el in valors]
        print(llTuples)
        
        for i in range(len(llTuples)):
            print("l'element",llTuples[i][0],"apareix",llTuples[i][1],"vegades a la llista")

    elif opcio == 11:
        
        #AFAGEIXO UN NOU VALOR '20'(Enter) A LA POSICIÓ 3 DE LA TUPLA
        #ja que tots els elements eren iterables, i no podia comprovar el 'try','except'
        aTuple = ("Orange", [10, 20, 30], (5, 15, 25), 20)
        valor = 20
        print(aTuple)   
        #for per recorrer posicions de la tupla
        for i in range(len(aTuple)):
            #mirar si l'element és iterable
            try: 
                iterable = iter(aTuple[i])
                #print(iterator)
            #si dóna error de tipus TypeError vol dir que no és iterable
            #controlem excepció
            except TypeError: 
                #print("no iterable")
                #mirem si trobem el valor a la posició de la tupla
                if aTuple[i] == valor:
                    print("\nValor",valor,"a posició:",i,"de la",type(aTuple))
            #si no dóna error, vol dir que l'element és iterable
            #per tant, recorrarem l'element iterable de dins la tupla
            else:
                #print("si iterable")
                for j in range(len(aTuple[i])):
                #print(el[i])
                    if aTuple[i][j] == valor:
                        print("\nValor",valor,"a posició:",i,"-",j)
                        print("Posició",i,"dins de",type(aTuple))
                        print("Posició",j,"dins de",aTuple[i],type(aTuple[i]))
    else:
        print("Opció incorrecte")

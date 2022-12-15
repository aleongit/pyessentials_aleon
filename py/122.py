#Aleix Leon

#factorial. Funcionalitat: Calcula el factorial d'un número (un enter no negatiu).
#La funció accepta el nombre com a paràmetre i retorna el factorial, o bé un error (-1),
#el missatge d’error s’imprimirà després de la crida.
#exemple: 5! = 1 x 2 x 3 x 4 x 5 = 120
def factorial(n):
    #si n positiu
    if n >=0:
        print(n,"--> ",end="")
        fac = 1
        for i in range(1,n+1):
            fac *= i #fac = fac * i
            #presentació
            if i != n:
                print(i,"x ",end="")
            else:
                print(i,"=",fac)
        print()   
    #si n negatiu
    else:
        fac = -1
    return fac

#comptaMajusMinus. Funcionalitat: accepta una cadena com a paràmetre
#i retorna el nombre de lletres majúscules i minúscules.
#'Una Cadena De Prova' Sortida esperada: (4,12). El missatge es mostra després de la crida. 
def comptaMajusMinus(cadena):
    maju = len([ll for ll in cadena if ll.isupper()]) #isupper() = mira si majúscules
    minu = len([ll for ll in cadena if ll.islower()]) #islower() = mira si minúscules
    return (maju,minu)

#llistaUnitaria. Funcionalitat: Donada una  llista que li passem com paràmetre,
#retorna una nova llista amb elements únics de la primera llista.
#Llista de mostres: [1,2,3,3,3,3,4,5] Llista unitària: [1, 2, 3, 4, 5]. No es pot utilitzar la comanda set.

def llistaUnitaria(llista):
    #versió for afegint a nova llista
    llU = []
    for el in llista:
        if el not in llU:
            llU.append(el)
    return llU

#primer. Funcionalitat: Escriu una funció Python que pren un nombre com a paràmetre menor que 10000
#i comproveu si el número és primer o no, o bé error.
#(podeu utilitzar l’algoritme del sedàs d’Eratòstanes)

def primer(Max):
    #Programa l’algorisme del sedàs d’Eratòstanes.
    
    #número primer ha de ser > 1
    if (Max < 2) or (Max > 9999):
        r = "Error"
    else:
        #declaració
        Min = 2
        marca = "."
        valors =[]

        #generar N valors a llista segons opció
        for i in range(Max + 1):
            valors.append(i)

        #algorisme
        for i in range(Min, int((Max)**(1/2)) + 1):
            #print(i)
            if valors[i] != marca:
                for j in range(i, ((Max) // i) + 1):
                    #print("la i",i,"-la j",j)
                    #print(i*j)
                    valors[i*j] = marca

        #print("\nTaula Marcats", valors)
        
        #busco si no està marcat
        if Max in valors:
            r = "És primer"
        else:
            r = "NO és primer"
    return r

#parells: Funcionalitat: Retorna els números parells d'una llista determinada passada com paràmetre.
#Llista de mostres: [1, 2, 3, 4, 5, 6, 7, 8, 9] Resultat esperat: [2, 4, 6, 8]
def parells(llista): 
    llP = [el for el in llista if el % 2 == 0]
    return llP

#perfecte: Funcionalitat: Escriviu una funció Python per comprovar si un número és perfecte o no.
#Segons Wikipedia: En la teoria de nombres, un nombre perfecte és un enter positiu
#que és igual a la suma dels seus divisors positius correctes,
#és a dir, la suma dels seus divisors positius excloent el nombre en si
#(també conegut com la seva suma alíquota).
#De forma equivalent, un nombre perfecte és un nombre que és
#la meitat de la suma de tots els seus divisors positius (incloent-hi).
#Exemple: el primer nombre perfecte és 6, perquè 1, 2 i 3 són els seus divisors positius correctes,
#i 1 + 2 + 3 = 6.
#Igualment, el número 6 és igual a la meitat de la suma de tots els seus divisors positius:
#(1 + 2 + 3 + 6) / 2 = 6.
#28 = 1 + 2 + 4 + 7 + 14
#496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
#8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064

def perfecte(n):
    #afageixo a llista els divisors
    llP = [i for i in range(1,n) if n % i == 0]
    
    #mostro els elements format suma
    print(*llP, sep=" + ",end =" = ")
    print(sum(llP))
    
    #suma divisors
    if n == sum(llP):
        r = "Número Perfecte"
    else:
        r = "NO és Número Perfecte"
    return r

#palíndrom: Funcionalitat: verifica si una cadena passada com paràmetre és palíndrom o no.
def palindrom(cadena):
    #depurar cadena
    
    #trec símbols i espais
    simbols = "-!?,.·' "
    llCadena = [ll for ll in cadena if ll not in simbols]
    
    #treure accents
    #versió amb str.maketrans() i str.translate()
    #(la documento perquè l'he trobat interessant)
    #cadenes de mateixa longitud per a conversió caràcter 1 a 1
    voAmb = 'àáèéíïòóúü'
    voSense ='aaeeiioouu'
    #taula de conversió de les dues cadenes
    dTaula = str.maketrans(voAmb,voSense)
    #print(dTaula, type(dTaula))
    #fer la conversió amb translate()
    print(cadena.translate(dTaula))
    
    #versió amb fors    
    #cal passar a llista, assignació per index a str no funciona
    #cadena =list(cadena)
    
    #per cada lletra de cadena
    for i in range(len(llCadena)):        
        #si té accent
        if llCadena[i] in voAmb:
            #busca posició a cadena AMB accents
            for j in range(len(voAmb)):
                #assigna l'equivalent quan el troba
                if llCadena[i] == voAmb[j]:
                    llCadena[i] = voSense[j]
                                
    #per tornar de llista a cadena
    #cadena = "".join(cadena)
    
    print("".join(llCadena))
    #giro cadena
    print("".join(llCadena[::-1]))
    
    #si la cadena = que cadena girada
    if  llCadena == llCadena[::-1]:
        r = "És un Palíndrom"
    else:
        r = "No és un Palíndrom"
    return r

#funció per menú
def fMenu(t,d):
    op = 1
    while op != 0:
        print("\n",t,"\n==============")
        for el in d:
            print (el, d[el])
        op = int(input("\nOpció: "))
        
        if op == 1:
            num = int(input("Número per factorial: "))
            #resultat
            r = factorial(num)
            if r == -1:
                print("*FATAL ERROR*: No es pot fer factorial de número negatiu")
            else:
                print(f"La factorial de {num} és {r}")
                
        elif op == 2:
            cadena = input("Cadena: ")
            print(comptaMajusMinus(cadena))
            
        elif op == 3:
            llista = [1,2,3,3,3,3,4,5]
            print(llistaUnitaria(llista))
            
        elif op == 4:
            num = int(input("Número per primer [2-9999]: "))
            print(f"{num} {primer(num)}")
            
        elif op == 5:
            llista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print(parells(llista))
        
        elif op == 6:
            num = int(input("Número per perfecte: "))
            print(f"{num} {perfecte(num)}")
            
        elif op == 7:
            cadena = input("Cadena per palíndrom: ")
            #cadena = "Català, a l'atac!"
            #quan passo transformo a mínuscules
            print(f"\n{palindrom(cadena.lower())}")

#Palíndrom: Frases en català
#-------------------------------------
# Anul·la la lluna
# Apa! Cal a la capa?
# Argentina, la lluna anul·la la nit negra
# Atrapa'l o l'aparta!
# A treballar allà, Berta!
# A una nena nua llepa-li la pell, llepa-li la pell a una nena nua
# Català, a l'atac!
# Cita-la a l'àtic
# El bo plau al poble.
# És així, ase!
# I ara calla, carai!
# I ara rai.
# Margarida dirà gram.
# Margarita tira gram
# No sap pas on!
# Salta l'airós nen sorià l'atlas.
# Senén té sis nens i set nenes.
# Sé on no és.
# S'és o no s'és.
# Tapa i àpat.
# Tramaran anar a Mart.
# El bé fa mal i la mà, feble.
# Sorra a la boda i adoba l'arròs.
# I rimeu que rimi i mireu que rimi! I mireu que miri!

#programa principal
            
#nota: id(variable) retorna id memòria, per saber si la variable és la mateixa un cop passada a la funció
# (pas per valor = simple / pas per ref = comple)

titol = "Funcions 2"
dOpcions = {1:"factorial",2:"comptaMajusMinus", 3:"llistaUnitaria",4:"primer",5:"parells",6:"perfecte",7:"palíndrom",0:"SORTIR"}

fMenu(titol,dOpcions)
 

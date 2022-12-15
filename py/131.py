# Aleix Leon

import random

# funció extra que comprova si matriu està buida o no
def existeixMatriu(matriu):
    existeix = False
    if matriu != [[]]:
        existeix = True
    return existeix

# funció extra per demanar versió
def versio():
    v=0
    while v!= 'n' and v!= 'c':
            # .lower() transformem a mínuscules l'entrada
            v = input("Versió normal o comprehension (n/c): ").lower()
    return v
        
# funció matriu2d, que li passes 2 nombres enters n1, n2
# i retorna una matriu m de 2 dimensions n1 x n2 plena de nombres aleatoris entre l’1 i el 100.
# versió matriu comprehension
def matriu2d_comp(n1,n2):
    #per i n1 files / j n2 columnes
  m = [[random.randint(1,100) for j in range(n2)]  for i in range(n1)]
  return m

# versió matriu amb dos fors (i = files / j = columnes)
def matriu2d(n1,n2):
    m=[] # matriu en blanc
    for i in range(n1): # per n1 files
      fila = [] # fila en blanc
      for j in range(n2): # per n2 columnes
        fila.append(random.randint(1,100)) #valor random
      m.append(fila) # afegim fila a matriu (m)
    return m

# funció printMatriu, que imprimeix la matriu que li passes com a paràmetre de manera similar a l’exemple:
# a b c d \t = valors tabulats a la dreta
# a b c d
def printMatriu(m):
    print(f"\nMatriu de {len(m)} x {len(m[0])} \n--------------------")
    for elx in m:
        for ely in elx:
            # control dígits (1, 2 o 3) per número espais, per alineació número a la dreta
            # 1 dígit posa 2 espais davant
            if len(str(ely)) == 1:
                print(f"  {ely}",end=" ")
            # 2 dígits posa 1 espais
            elif len(str(ely)) == 2:
                print(f" {ely}",end=" ")
            # cas 3 dígits no espais davant
            else:
                print(f"{ely}",end=" ")
        print()

#funció print simple amb espai
def printMatriuTab(m):
    for el in m:
        print(*el, sep =" ")
        
# funció llistaMultiples que li passes la matriu m de 2 dimensions com a argument,
# i un enter e entre l’1 i el 10
#i retorna una llista ll d’1 dimensió formada pels múltiples d’e existents a la matriu.
#versió comprehension
def llistaMultiples_comp(m,e):
    ll = [n for fila in m for n in fila if n % e == 0]
        #[x for b in a for x in b]
    return ll

#versió for normal
def llistaMultiples(m,e):
    ll=[]
    for fila in m:
        for n in fila:
            if n % e == 0:
                ll.append(n)
    return ll 

# funció llistaUnica que li passes la matriu m i retorna una llista única (sense repetits) d’1 dimensió.
# versió comprehension
def llistaUnica_comp(m):
    #generem set (únics) que passem a llista ordenada
    ll = list({n for fila in m for n in fila})
    ll.sort()
    return ll

# versió for normal
def llistaUnica(m):
    #llista buida
    llista=[]
    for fila in m:
        for n in fila:
            if n not in llista:
                llista.append(n)
    llista.sort()
    return llista

# funció minMax que retorna el mínim i el màxim de la matriu m que li passes com a paràmetre.
# versió comprehension
def minMax_comp(m):
    #max i mínim de tots els valors en llista
    mx = max([n for fila in m for n in fila])
    mn = min([n for fila in m for n in fila])
    return mn,mx

#funció amb dos for per index
def minMax(m):
    #Assignem el primer element de la matriu com a inicialitzador
    maxim = m[0][0]
    minim = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>maxim:
                maxim=m[i][j]
            if m[i][j]<minim:
                minim=m[i][j]
    return minim,maxim

# funció acabaEn que li passes la matriu m com a argument, i un enter e entre l’0 i el 9
# i retorna una llista d’1 dimensió formada pels nombres que la seva última xifra és e.
#versió comprehension
def acabaEn_comp(m,e):
    #agafem valor que última posició = enter, convertint a str()
    ll = [n for fila in m for n in fila if str(n)[-1] == str(e)]
    return ll

#versió dos fors
def acabaEn(m,e):
    ll=[]
    for fila in m:
        for n in fila:
            if str(n)[-1] == str(e):
                ll.append(n)
    return ll

# funció quadrat que donat un sencer s entre 10 i 20 retorna una matriu quadrada de 2 dimensions
#de mida s x s inicialitzada al caràcter que li passes com a segon paràmetre.
# versió comprehension
def quadrat_comp(e,c):
    m = [[c for j in range(e)] for i in range(e)]
    return m

#versió dos fors
def quadrat(e,c):
    #dimensió 1
    m=[]
    for i in range(e):
        #dimensió 2
        fila=[]
        for j in range(e):
            fila.append(c)
            #fila += [c]
        m.append(fila)
        #m += [fila]
    return m

# funció inicialitza que inicialitza tots els elements de la matriu al caràcter que li passes per argument.
# (arguments, la matriu q i el caràcter c).
def inicialitza(m,c):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = c
    #no cal retornar matriu, pas per referència
    #return m

# funció diagonal que posa en les diagonals de la matriu quadrada q, el caràcter c.
# Es passen com a paràmetres de la funció q i c.
def diagonal(m,c):
    for i in range(len(m)):
        for j in range(len(m[i])):
            #diagonal de esquerra a dreta
            #(0,0) (1,1) (2,2) ...
            if i == j:
                m[i][j] = c
            #diagonal de dreta a esquerra
            #(0,10) (1,9) (2,8) ...
            elif j == len(m[-1])-i -1:
                m[i][j] = c           
    #no cal retornar matriu, pas per referència
    #return m

# funció creu que rep 2 paràmetres n i c:
#Comprova que n sigui un nombre senar positiu sinó retorna “error”.
#Genera una matriu quadrada de mida n x n, amb tots el elements “ “.
#Forma una creu amb el caràcter c, és a dir, tots els elements de la columna del mig han de ser el caràcter c i tots els elements de la fila del mig han de ser el caràcter c.
def creu(m,n,c):
    senar = True
    #control senar
    if n % 2 == 0:
        senar = False
    else:
         for i in range(len(m)):
            for j in range(len(m[i])):
                #línies meitat
                if (i == len(m) // 2) or (j == len(m[0]) // 2):
                    m[i][j] = c
         #printMatriu(m)
    return senar

# funció per menú
def fMenu():
    titol = "Funcions i matrius 2D"
    ll = ["sortir","matriu2d","printMatriu","llistaMultiples","llistaUnica","minMax",\
            "acabaEn ","quadrat ","inicialitza","diagonal","creu"]
    
    print("\n",titol,"\n-----------------------")
    for i in range(len(ll)):
        print (f"{i}\t{ll[i]}")
    
    #control visual per veure si les matrius estan generades (matriu i matriu quadrada)
    print("* Matriu números:",*m, sep = " ")
    print("* Quadrat generat:",existeixMatriu(mq))
            
# programa principal

#inicialitzem matrius
m = [[]]
mq = [[]]
 
op = 1
while op != 0:
    fMenu()
    op = int(input("\nOpció: "))
    
    if op == 1:
        v = versio()
        n1 = int(input("n1 (files): "))
        n2 = int(input("n2 (cols) : "))
        if v == 'n':
            #amb abs() no acceptem valors negatius
            m = matriu2d(abs(n1),abs(n2))
        else:
            m = matriu2d_comp(abs(n1),abs(n2))
        print()
        print(*m,sep = "\n")
            
    elif op == 2:
        #si no s'ha generat matriu (m), genera
        if not existeixMatriu(m):
            #generem amb random dimensions
            m = matriu2d(random.randint(1,10),random.randint(1,10))
        printMatriu(m)
        print()
        #printMatriuTab(m)
        
    elif op == 3:
        v = versio()
        #control enter
        e = 0
        while e < 1 or e > 10:
            e = int(input("Enter [1-10]: "))
        if not existeixMatriu(m):
            m = matriu2d(random.randint(1,10),random.randint(1,10))
        #imprimim matriu
        printMatriu(m)
        #crida
        if v == 'n':
            print(f"\nMúltiples de {e} :",*(llistaMultiples(m,e)),end =" ")
        else:
            print(f"\nMúltiples de {e} :",*(llistaMultiples_comp(m,e)),end =" ")
        print()
            
    elif op == 4:
        v = versio()
        if not existeixMatriu(m):
            m = matriu2d(random.randint(1,10),random.randint(1,10))
        #imprimim matriu
        printMatriu(m)
        if v == 'n':
            print("\nElements únics:",*(llistaUnica(m)),end =" ")
        else:
            print("\nElements únics:",*(llistaUnica_comp(m)),end =" ")
        print()
        
    elif op == 5:
        v = versio()
        if not existeixMatriu(m):
            m = matriu2d(random.randint(1,10),random.randint(1,10))
        #imprimim matriu
        printMatriu(m)
        if v == 'n':
            print(f"\nminMax:",minMax(m))
        else:
            print(f"\nminMax:",minMax_comp(m))
        print()
    
    elif op == 6:
        v = versio()
        #control enter
        e = -1
        while e < 0 or e > 9:
            e = int(input("Enter [0-9]: "))
        if not existeixMatriu(m):
            m = matriu2d(random.randint(1,10),random.randint(1,10))
        #imprimim matriu
        printMatriu(m)
        if v == 'n':
            print(f"\nacabaEn {e}:",acabaEn(m,e))
        else:
            print(f"\nacabaEn {e}:",acabaEn_comp(m,e))
        print()
        
    elif op == 7:
        v = versio()
        #control enter
        e = 0
        while e < 10 or e > 20:
            e = int(input("Enter [10-20]: "))
        c = ""
        while c == "":
            c = input("Caràcter: ")
        if v == 'n':
            mq = quadrat(e,c)
        else:
            mq = quadrat_comp(e,c)
        #imprimim matriu
        printMatriu(mq)
    
    elif op == 8:
        #si no s'ha generat quadrat (mq), genera
        if not existeixMatriu(mq):
            mq = quadrat(random.randint(10,20),'-')
        #imprimim matriu
        printMatriu(mq)
        print()
        c = ""
        while c == "":
            c = input("Inicialitzem Caràcter: ")
        inicialitza(mq,c)
        #imprimim matriu
        printMatriu(mq)
    
    elif op == 9:
        if not existeixMatriu(mq):
            mq = quadrat(random.randint(10,20),'-')
        #imprimim matriu
        printMatriu(mq)
        print()
        c = ""
        while c == "":
            c = input("Caràcter diagonal: ")
        diagonal(mq,c)
        #imprimim matriu
        printMatriu(mq)
                
    elif op == 10:
        #generem matriu amb diagonal (valors per defecte) si no existeix
        if not existeixMatriu(mq):
            mq = quadrat(random.randint(10,20),'-')
            diagonal(mq ,'*')            
        #mirem mida de mq generada
        n = len(mq)
        print(n)
        #demanem caràcter creu
        c = ""
        while c == "":
            c = input("Caràcter creu: ")
        #cridem per fer 'creu' i que retorna bolèa si senar o no
        #COMPTE ANUNCIAT! a l'anunciat diu que funció creu  rep 2 paràmetres n i c
        #però en l'exemple de crida envia matriu enlloc de n: creu(qua,"|")
        #així que enviarem 3 paràmetres (matriu, mida, caràcter)
        #mentre no sigui senar, demanem nova mida, generem matriu amb mida,
        #guardant caràcters anteriors, i tornem a enviar a funció 'creu'
        while not creu(mq,n,c):
                print("*ERROR MIDA*")
                #demanem nova mida
                n=0
                while n < 10 or n > 20:
                    n = int(input("Mida matriu senar [10-20]: "))
                #agafem caràcter quadrat existent
                cq = mq[0][1]
                #agafem caràcter diagonal existent
                cd = mq[0][0]
                #crem nou quadrat amb nova mida aprofitant caràcters
                mq = quadrat(n,cq)
                diagonal(mq,cd)
        printMatriu(mq)
 
# Aleix Leon

import random

# 1
# funció absolut que faci el mateix que la funció incorporada de Python abs()
# passant-li un nombre (enter o un float).

# abs()
# Return the absolute value of a number:
# x = abs(-7.25)

def absolut(r):
    #comprovem tipus admesos
    tipus = (int,float)
    #print(isinstance(r,tipus))
    if not isinstance(r,tipus):
        r = None
    else:
        #si número negatiu, multipliquem per -1
        if r < 0:
            r *= -1
    return r

# 2
# funció elevar que faci el mateix que la funció incorporada de Python pow()
# passant-li 2 enters, 2 floats, 1 enter i 1 float o 1 float i 1 enter.

# pow(x, y, z)
# x   A number, the base
# y   A number, the exponent
# z   Optional. A number, the modulus

# Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
# x = pow(4, 3, 5)

def elevar(base,exp):
    #comprovem tipus admesos
    
    #CONDICIONS TAL QUAL ENUNCIAT, UNA MICA LLEIG
    #if not ((isinstance(base,int) and isinstance(exp,int)) or \
    #        (isinstance(base,float) and isinstance(exp,float)) or \
    #        (isinstance(base,int) and isinstance(exp,float)) or \
    #        (isinstance(base,float) and isinstance(exp,int))):
    
    tipus = (int,float)
    #si base i exponent són int o float
    if not (isinstance(base,tipus) and isinstance(exp,tipus)):
        r = None
    else:
        r = base**exp
    return r

#3
# funció longitud que faci el mateix que la funció incorporada de Python len()
# passant-li una cadena, una llista o un iterable.

# The len() function returns the number of items in an object.
# When the object is a string, the len() function returns the number of characters in the string.
# x = len(mylist)

def longitud(n):
    #comprovem tipus admesos
    #canviem a funció iter() ja que així controlem tots els iterables com diu l'enunciat
    try:
        iter(n)
    except TypeError:
        #print("no iterable")
        r = None
    else:
        #print("iterable")
        r = 0
        for el in n:
            r += 1
    return r

# 4
# funció alreves que faci el mateix que la funció incorporada (mètode) de
# Python list.reverse() passant-li una llista.

def alreves(ll):
    #comprovem tipus admesos
    tipus =(list)
    if not isinstance(ll,tipus):
        r = None
    else:
        r = ll[::-1]
    return r

# 5
# funció elevar que faci el mateix que la funció incorporada de Python pow()
# passant-li 3 enters (el darrer enter serveix per calcular el mòdul).

# pow(x, y, z)
# x   A number, the base
# y   A number, the exponent
# z   Optional. A number, the modulus

# Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
# x = pow(4, 3, 5)

def elevar_modul(base,exp,mod):
    #comprovem tipus admesos
    tipus = (int)
    #si base, exponent i mòdul són int
    if not (isinstance(base,tipus) and isinstance(exp,tipus) and isinstance(mod,tipus)):
        r = None
    else:
        r = (base**exp) % mod
    return r

# 6
# funció maxim que faci el mateix que la funció incorporada de Python max()
# passant-li una llista d’enters o una llista de cadenes de caràcters.

# The max() function returns the item with the highest value,
# or the item with the highest value in an iterable.
# If the values are strings, an alphabetically comparison is done.
# x = max("Mike", "John", "Vicky")
# a = (1, 5, 3, 9)

def maxim(ll):
    #comprovem tipus admesos
    tipus =(list)
    if not isinstance(ll,tipus):
        r = None
    else:
        #màxim
        #inicialitzem per 1r valor llista
        maxim = ll[0]
        for el in ll:
            if el > maxim:
                maxim = el
        r = maxim   
    return r

# 7
# funció suma que faci el mateix que la funció incorporada de Python sum()
# passant-li un iterable (pot ser una llista o una tupla) de nombres.
# Opcionalment es pot passar un valor a afegir a la suma.

# The sum() function returns a number, the sum of all items in an iterable.
# iterable    Required. The sequence to sum
# start       Optional. A value that is added to the return value
# a = (1, 2, 3, 4, 5)
# x = sum(a, 7)

def suma(valors,*v):
    #comprovem tipus admesos
    tipus =(list,tuple)
    if not isinstance(valors,tipus):
        r = None
    else:
        #control valor opcional
        #tipus tupla
        #print(type(op))
        #si tupla és buida (sense opcional) op = 0
        if v == ():
            op = 0
        #sinó agafem valor opcional de tupla 1a pos
        else:
            op =v[0]
        #sumem
        #inicialitzem acumulador
        s = 0
        for el in valors:
            s += el
        r = s + op
    return r

# 8
# funció ordenat que faci el mateix que la funció incorporada de Python sorted()
# passant-li una llista o una tupla.
# Dels paràmetres opcionals que té la funció incorporada, programa el reverse
# que indica si s’ordena ascent o descent.

# The sorted() function returns a sorted list of the specified iterable object.
# You can specify ascending or descending order.
# Strings are sorted alphabetically, and numbers are sorted numerically.

#iterable    Required. The sequence to sort, list, dictionary, tuple etc.
#key         Optional. A Function to execute to decide the order. Default is None
#reverse     Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

# Sort descending:
# a = ("h", "b", "a", "c", "f", "d", "e", "g")
# x = sorted(a, reverse=True)

def ordenat(v,*o):
    
    #comprovem tipus admesos
    tipus =(list,tuple)
    if not isinstance(v,tipus):
        r = None
    else:
        #si és tupla passem a llista
        #print(type(v))
        if type(v) == tuple:
            v = list(v)
            #print(type(v))
 
        #ordenem per nan perquè bombolla sempre fot coses rares
        pos = 0
        #fins que no arribem al final de llista
        while pos < len(v): 
            #si està al principi o la posició és més gran que l'anterior, continua amb la llista
            if pos == 0 or v[pos] >= v[pos-1]:
                pos += 1
            #si la posició anterior és mes gran que la actual, tire enrrere la posició actual
            else:
                #intercanviem posició amb posició anterior
                guarda = v[pos]
                v[pos] = v[pos-1]
                v[pos-1] = guarda
                #decrementem posició, tornem enrere
                pos -= 1
        
        #paràmetre opcional ordenació, compte és tupla!
        if len(o) == 1 and o[0]:
            v = alreves(v)
        r = v
        return r

# 9
# funció rang que faci el mateix que la classe incorporada de Python range()
#passant-li 1 enter que indica el final del rang.
#La nostra funció retornarà una llista o una tupla amb els valors generats.
# 10
# funció rang que faci el mateix que la classe incorporada de Python range()
#passant-li 2 o 3 enters que indiquen l’inici del rang,i el final del rang i el pas.
#La nostra funció retornarà una llista o una tupla amb els valors generats.
#Es pot fer modicant l’anterior (ha de continuar funcionant) o fer-ne una versió nova.

# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# start   Optional. An integer number specifying at which position to start. Default is 0
# stop    Required. An integer number specifying at which position to stop (not included).
# step    Optional. An integer number specifying the incrementation. Default is 1

# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
# x = range(3, 20, 2)

#prova amb només pas de tupla arguments opcionals
def rang(*t):
    
    #inicializem arguments per defecte
    start = 0
    stop = 0
    step = 1
    ll = []
    ok = True
    
    #agafem mida tupla arguments
    mida = len(t)
    
    #comprovem tipus dels 3 possibles arguments
    for el in t:
        if not isinstance(el,int):
            ok = False
    if not ok:
        r = None
    else:
        #cas 1 paràmetre (stop)
        if mida == 1:
            stop  = t[0]
        
        elif mida == 2:
            start = t[0]
            stop  = t[1]
        
        elif mida == 3:
            start = t[0]
            stop  = t[1]
            step  = t[2]
        
        #comptador
        cont = start
        #fem rang amb while
        while cont < stop:
            ll.append(cont)
            cont += step
        r = ll
    return r

# funció per menú
def fMenu():
    titol = "Funcions Incorporades"
    ll = ["sortir","absolut","elevar","longitud","alreves","elevar_modul","maxim",\
            "suma ","ordenat ","rang","rang (v2)"]
    
    print("\n",titol,"\n-----------------------")
    for i in range(len(ll)):
        print (f"{i}\t{ll[i]}")
            
# programa principal

# declaració
e = 5
en = -7
f = 5.55
fn = -3.5
s = "Això és una cadena"
abc = "abcdefghijklmnopqrstuvwxyz"
num = "123456789"
t = (1,2,3,4)
ll = ['a','b','c','d','e']
tipus = ()

op = 1
while op != 0:
    fMenu()
    op = int(input("\nOpció: "))
    
    if op == 1:
        
        #for per provar varis tipus de valors
        valors = (e,en,f,fn,s,t)
        print("Provem funció amb diversos tipus de valors")
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if absolut(el) != None:
                print(f"\nAbsolut de nombre {el} de tipus {type(el)}")
                print(f"absolut(): {absolut(el)}")
                print(f"abs()    : {abs(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {absolut(el)} per {type(el)}")
            
    elif op == 2:
        
        #per provar varis tipus de valors
        valors = (e,en,f,fn,s,t)
        
        #tipus de valors aleatori
        n1 = random.choice(valors)
        n2 = random.choice(valors)
        print(n1,n2)
        
        print("Provem funció amb tipus de valors aleatoris")
        
        if elevar(n1,n2) != None:
            print(f"\nPotència de nombre {n1} tipus {type(n1)} elevat a {n2} tipus {type(n2)}")
            print(f"elevar(): {elevar(n1,n2)}")
            print(f"pow():    {pow(n1,n2)}")
        #si retorna None
        else:
            print(f"\nRetorna {elevar(n1,n2)} per base {type(n1)} i exponent {type(n2)}")
    
    elif op == 3:
        
        #for per provar varis tipus de valors
        valors = (e,f,s,t,ll)
        
        print("Provem funció amb diversos tipus de valors")
        
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if longitud(el) != None:
                print(f"\nLongitud de {el} de tipus {type(el)}")
                print(f"longitud(): {longitud(el)}")
                print(f"len()     : {len(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {longitud(el)} per {type(el)}")
            
    elif op == 4:
        
        #for per provar varis tipus de valors
        valors = (e,f,s,t,ll)
        
        print("Provem funció amb diversos tipus de valors")
        
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if alreves(el) != None:
                print(f"\n{el} de tipus {type(el)}")
                print(f"alreves()     : {alreves(el)}")
                el.reverse()
                print(f"list.reverse(): {el}")
            #si retorna None
            else:
                print(f"\nRetorna {alreves(el)} per {type(el)}")
        
    elif op == 5:
        
        #per provar varis tipus de valors (int i float)
        #es generen 3 enters i un float (random.uniform) a la llista de valors
        valors = (random.randint(10,20),random.randint(1,10),random.randint(1,5),random.uniform(1,10))
        
        print("Provem funció amb diversos tipus de valors aleatoris")
        print(valors)
        
        #es seleccionen valors de la llista
        n1 = random.choice(valors)
        n2 = random.choice(valors)
        n3 = random.choice(valors)
        print(n1,n2,n3)
        
        if elevar_modul(n1,n2,n3) != None:
            print(f"\nPotència de nombre {n1} tipus {type(n1)} elevat a {n2} tipus {type(n2)} i mòdul {n3} tipus {type(n3)}")
            print(f"elevar_modul(): {elevar_modul(n1,n2,n3)}")
            print(f"pow()         : {pow(n1,n2,n3)}")
        #si retorna None
        else:
            print(f"\nRetorna {elevar_modul(n1,n2,n3)} per base {type(n1)}, exponent {type(n2)} i mòdul {type(n3)}")
    
    elif op == 6:
        
        #definim llistes aleatòries
        #lln = [el for el in num]
        #creació llista núms aleatoris de mides aleatories de valors extrets d'una cadena
        lln = [int("".join(["".join(random.choice(num)) for n in range(int(random.choice(num)))])) for i in range(int(random.choice(num)))]
        #llc = ["".join(random.choice(abc)) for i in range(5)]
        #creació llista strings aleatòries de mides aleatòries de valors extrets d'una cadena
        llc = ["".join(["".join(random.choice(abc)) for p in range(int(random.choice(num)))]) for i in range(int(random.choice(num)))]
        
        print("Generats iterables aleatoris:")
        print(lln)
        print(llc)
        
        print("\nProvem funció amb diversos tipus de valors aleatoris")
        
        #for per provar varis tipus de valors
        valors = (lln,llc,s,e)
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if maxim(el) != None:
                print(f"\nMàxim de {el} de tipus {type(el)}")
                print(f"maxim(): {maxim(el)}")
                print(f"max()  : {max(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {maxim(el)} per {type(el)}")
        
    elif op == 7:
        
        #generem iterables
        #llista aleatòria
        lln = [random.randint(1,100) for n in range(random.randint(5,10))]

        #tupla aleatòria
        tn = tuple([random.randint(1,100) for n in range(random.randint(5,10))])
        
        print("Generats iterables aleatoris:")
        print(lln)
        print(tn)
        
        print("\nProvem funció amb diversos tipus de valors aleatoris")
        
        #for per provar varis tipus de valors
        valors = (lln,tn,s,e)
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if suma(el) != None:
                print(f"\nSuma de {el} de tipus {type(el)}")
                print(f"suma(): {suma(el)}")
                print(f"sum() : {sum(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {suma(el)} per {type(el)}")
        
        #provem amb paràmetre opcional
        print("\nProvem funció amb valor afegit opcional aleatori")
        
        v = random.randint(1,10)
        print(v)
        #for per provar varis tipus de valors
        valors = (lln,tn)
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if suma(el,v) != None:
                print(f"\nSuma de {el} de tipus {type(el)} amb pas valor {v} opcional de tipus {type(v)}")
                print(f"suma(): {suma(el,v)}")
                print(f"sum() : {sum(el,v)}")
            #si retorna None
            else:
                print(f"\nRetorna {suma(el,v)} per {type(el)}")
    
    elif op == 8:
        
        #generem iterables
        #llista aleatòria
        lln = [random.randint(1,100) for n in range(random.randint(5,10))]

        #tupla aleatòria
        tc = tuple(["".join(["".join(random.choice(abc)) for p in range(random.randint(5,10))]) for i in range(random.randint(5,10))])
        
        print("Generats iterables aleatoris:")
        print(lln)
        print(tc)
        
        print("\nProvem funció amb diversos tipus de valors aleatoris")
        
        #for per provar varis tipus de valors
        valors = (lln,tc,s,e)
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if ordenat(el) != None:
                print(f"\nOrdenació de {el} de tipus {type(el)}")
                print(f"ordenat(): {ordenat(el)}")
                print(f"sorted() : {sorted(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {ordenat(el)} per {type(el)}")
        
        #provem amb paràmetre opcional
        #for per provar varis tipus de valors
        valors = (lln,tc)
        
        print("\nProvem funció amb valor afegit reverse")
        
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if ordenat(el,True) != None:
                print(f"\nOrdenació de {el} de tipus {type(el)} amb reverse=True")
                print(f"ordenat(): {ordenat(el, True)}")
                print(f"sorted() : {sorted(el, reverse=True)}")
            #si retorna None
            else:
                print(f"\nRetorna {ordenat(el,True)} per {type(el)}")
    
    elif op == 9:
        
        print("\nProvem funció amb diversos tipus de valors aleatoris")
        
        #for per provar varis tipus de valors
        valors = (random.randint(5,10),s)
        
        for el in valors:
            #print(el)
            #si no retorna None fes funció programada i equivalent
            if rang(el) != None:
                print(f"\nRang de {el} de tipus {type(el)}")
                print(f"rang(): {rang(el)}")
                print(f"range() : {range(el)}")
            #si retorna None
            else:
                print(f"\nRetorna {rang(el)} per {type(el)}")
                
    elif op == 10:
        
        #generem valors per arguments
        ini = random.randint(0,3)
        fi = random.randint(10,100)
        pas = random.randint(1,5)
    
        if rang(ini,fi) != None:
            print("\ncrida 2 arguments")
            print(f"Rang de {ini} a {fi}")
            print(f"rang() : {rang(ini,fi)}")
            print(f"range(): {range(ini,fi)}")
        else:
            print(rang(ini,fi))
        
        if rang(ini,fi,pas) != None:
            print("\ncrida 3 arguments")
            print(f"Rang de {ini} a {fi} amb pas {pas}")
            print(f"rang() : {rang(ini,fi,pas)}")
            print(f"range(): {range(ini,fi,pas)}")
        else:
            print(rang(ini,fi,pas))

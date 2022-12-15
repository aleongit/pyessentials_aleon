#Aleix Leon

#inputs fora funció
#passo c = títol opció menú (per fer una prova)
def fMultiplica(a,b,c):
    print("\n", c,"\n", a, "x", b, "=", a*b)

#inputs dins funció
def f2000():
    #importo funció
    from datetime import datetime
    avui = datetime.now()
    #avui.year
    #avui.month
    #avui.day
    #print(avui.year,type(avui.year))
    a = int(input("\nAny actual ? "))
    if a != avui.year:
        print(f"\nNo cola! l'any actual és {avui.year}")
        a = avui.year 
    print(f"Des del 2000 han passat {a-2000} anys")

#tasca tiquet fruita tal qual
def fFruita():
    #declaració
    dPreu = {"poma":1.60,"pera":2.10,"cirera":3.20,"maduixa":5.10,"préssec":2.50}
    N = len(dPreu) #número de tipus de fruita
    dPes = {} #diccionari per pesos
    M = 8 #caràcters de tabulació
    dEspais = {} #diccionari per espais

    #demanem pes dins dun bucle for
    for el in dPreu:
        #Mentre no dongui l'ok, demana
        ok = False
        while ok == False:
            try:
                #guardo pesos a una llista
               #pesFruita[el] = "{:.2f}".format(float(input(f"Introdueix el pes de la fruita {el} en kg format(n.n):")))
               dPes[el] = float(input(f"Introdueix el pes de la fruita {el} en kg format(n.n):"))
            
            #controlem excepció
            except ValueError:
                print("format incorrecte")

            else:
                ok = True
    #print(dPes)

    #diccionari imports
    dImport = { el : dPreu[el]*dPes[el] for el in dPes }
    #print(dImport)

    #diccionari espais
    for el in dPreu:
        espais= ""
        for i in range(M - len(el)):
            espais += " "
        dEspais[el] = espais
    #print(dEspais)

    #també afageixo columna 'pes'
    print("\nLa fruiteria de l'Aleix: Tiquet de compra\n" \
          "============================================")
    for el in dImport:
        #"{:05.2f}".format = 5 posicions amb 0 a esquerra i 2 decimals float
        print(el, dEspais[el],":", dPreu[el], "€/kg ·", \
              "{:5.2f}".format(dPes[el]),"kg =>","{:05.2f}".format(dImport[el]),"€")

    print("\n===========================================")
    print("Import total: num ítems\t",len(dImport),"\t  ","{:05.2f}".format(sum(dImport.values())),"€")

def fNota(n1,n2):
#Només fa mitja si les dues notes són més grans o iguals que 4
#Nota Mòdul = 70% * NotaEx +30% * NotaPr
#Si la nota és més gran o igual que 5 arrodoneix
#i imprimeix el literal corresponent ( 5 Aprovat, 6 Bé, 7 8 Notable, 9 10 Excel·lent)
    dNotes = {5:'Aprovat',6:'Bé',7:'Notable',8:'Notable',9:'Excel·lent',10:'Excel·lent'}
#Si està suspès demana si ha comprat un pernil al professor/a. Si és que sí imprimeix “aprovat perniler”.
    sn ="sn"
    
    #control per nota mitja
    if n1 < 4:
        n1 = 0
    if n2 < 4:
        n2 = 0
    
    #càlcul nota
    nm = n1*0.70 + n2*0.30
    print(nm)
    #print(int(round(nm,0)))
    #arrodonim
    nm = int(round(nm,0))
    
    print(nm)
    #.get() retorna valor si clau existeix, sinó retorna 'Suspès'
    nf = dNotes.get(nm,'Suspès')
    #print(dNotes.get(nm,'Suspès'))
    print(nf)
    if nf == 'Suspès':
        r = "x"
        while r.lower() not in sn:
            r = input("Has comprat un pernil al professor/a? [s/n]: ")
        if r.lower() == "s":
            print("Aprovat Perniler")
        else:
            print("Suspès del tot")
            
#funció per menú
def fMenu(t,d):
    op = 1
    while op != 5:
        print("\n",t,"\n==============")
        for el in d:
            print (el, d[el])
        op = int(input("\nOpció: "))
        
        if op == 1:
            #print("\n",d[op])
            n1 = int(input("\nNúmero 1: "))
            n2 = int(input("Número 2: "))
            fMultiplica(n1,n2,d[op])
            
        if op == 2:
            f2000()
            
        if op == 3:
            fFruita()
            
        if op == 4:
            ne = float(input("\nNota Exàmen: "))
            np = float(input("Número Pràctiques: "))
            fNota(ne,np)

#programa principal
titol = "Funcions 1"
dOpcions = {1:"Multiplica",2:"Anys 2000", 3:"Tiquet Fruita", 4:"Nota UF",5:"SORTIR"}

fMenu(titol,dOpcions)
 

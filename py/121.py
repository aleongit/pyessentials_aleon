#Aleix Leon

#Funcionalitat: calcula i retorna el resultat de multiplicar dos números introduïts per teclat.
def Multiplica(a,b):
    return a*b

#Funcionalitat: Demana a l’usuari l’any actual i retorna: “Des del 2000 han passat x anys”,
#substituint la x pel nombre d’anys que han passat
def anys2000():
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
    return (a-2000)

#Funcionalitat: Demana la nota de l’examen i la nota de pràctiques. Fa el càlcul següent: 
#Només fa mitja si les dues notes són més grans o iguals que 4
#Nota Mòdul = 70% * NotaEx +30% * NotaPr
#Si la nota és més gran o igual que 5 arrodoneix i retorna el literal corresponent
#( 5 Aprovat, 6 Bé, 7 8 Notable, 9 10 Execel·lent)
#Si està suspès demana si ha comprat un pernil al professor.
#Si és que si retorna  “aprovat perniler”, sinó “Ens veiem al juny”

def notaUF():
    dNotes = {5:'Aprovat',6:'Bé',7:'Notable',8:'Notable',9:'Excel·lent',10:'Excel·lent'}
    sn ="sn"
    
    n1 = float(input("\nNota Exàmen: "))
    n2 = float(input("Número Pràctiques: "))
    
    #control per nota mitja
    if n1 < 4:
        n1 = 0
    if n2 < 4:
        n2 = 0
    
    #càlcul nota
    nm = n1*0.70 + n2*0.30

    #arrodonim
    nm = int(round(nm,0))
    
    #.get() retorna valor si clau existeix, sinó retorna 'Suspès'
    nf = dNotes.get(nm,'Suspès')

    if nf == 'Suspès':
        r = "x"
        while r.lower() not in sn:
            r = input("Has comprat un pernil al professor/a? [s/n]: ")
        if r.lower() == "s":
            nf = "Aprovat Perniler"
        else:
            nf = "Ens veiem al juny"
            
    return nf
            
#funció per menú
def fMenu(t,d):
    op = 1
    while op != 4:
        print("\n",t,"\n==============")
        for el in d:
            print (el, d[el])
        op = int(input("\nOpció: "))
        
        if op == 1:
            n1 = int(input("\nNúmero 1: "))
            n2 = int(input("Número 2: "))
            print(f"\n{n1} x {n2} = {Multiplica(n1,n2)}")
            
        if op == 2:
            print(f"Des del 2000 han passat {anys2000()} anys")
                
        if op == 3:
            print(f"\n{notaUF()}")
            

#programa principal
            
#nota: id(variable) retorna id memòria, per saber si la variable és la mateixa un cop passada a la funció
# (pas per valor = simple / pas per ref = comple)

titol = "Funcions 1"
dOpcions = {1:"Multiplica",2:"Anys 2000", 3:"Nota UF",4:"SORTIR"}

fMenu(titol,dOpcions)
 

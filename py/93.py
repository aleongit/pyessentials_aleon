#Aleix Leon
#Diccionaris

#Programar una bàscula d’una fruiteria. L’objectiu serà fer el tiquet de cada venda. Declara un diccionari.
#El diccionari tindrà com a clau el nom de les fruites, i com a valor el preu per kg de la fruita indicada
#(fes un diccionari que tingui 5 tipus de fruites diferents).
#Un cop creat el diccionari demana per cada fruita el pes, i acumula en una variable import.
#Has d’imprimir en un format net i polit un tiquet similar a l’exemple.
#Ajuda http://puntoflotante.org/languages/python/ 

#declaració
dPreu = {"poma":1.60,"pera":2.10,"cirera":3.20,"maduixa":5.10,"préssec":2.50}
N = len(dPreu) #número de tipus de fruita
dPes = {} #diccionari per pesos
M = 8 #caràcters de tabulació
dEspais = {} #diccionari per espais

#print(type(dPreu))
#print(dPreu)
#print(N)

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
#(amb \t no quedava a la mateixa tabulació, ja que depent de llargada nom)
#per cada clau de fruita, conto la dif d'espais entre valor definit (M) i llardada nom fruita
#creo una string d'espais de la llargada per cada fruita
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

#Aleix Leon

#MasterMind

#es generarà una seqüència aleatòria de mida 4 que serà una combinació de “ABCDE”,
#pot haver-hi lletres repetides, per exemple AABB, ACBD, ADAB, BBDC, etc.
#FOR concatenant random choise x lletra, tantes vegades com lletra
#l'usuari té 5 vides, és a dir 5 possibilitats per intentar encertar la combinació.

#Mentre no hagi encertat la combinació, i encara tingui vides fer:
#Resta una vida.
#Mostra els intents que ha fet fins el moment.
#Demana combinació per teclat i no avança fins que no sigui combinació possible
#(mida 4 i formada per les lletres possibles)
#Compta quantes lletres encertades estan en la posició correcta.
#Marca aquestes posicions per evitar comptar-les dues vegades.
#Compta quantes lletres encertades en posició incorrecta hi ha.
#Marca aquestes posicions per evitar comptar-les dues vegades.

#Si la combinació és guanyadora,
#Mostra missatge d’enhorabona i finalitza el programa.

#En altre cas:
#Mostra quines lletres en posició correcta hi ha amb el símbol #
#Mostra quines lletres encertades hi ha en posició incorrecta amb el símbol *
#Mostra les lletres no existents a la combinació amb el símbol -
#Per exemple si la combinació guanyadora és AACB i l’usuari entra ACDE ha de mostrar # * - -. La A és correcta i està en la posició correcta #, la C és correcta en posició incorrecta * i la resta D E no encertades, per tant - -.
#   A B C D
#   A A B B
    # - * * (La que encertem ja la marquem com encertada)

#CONSTANTS
MIDA = 4
VIDES = 5
TROBADA ="# # # # "

#variables
vida = 0
lletres_str = ""
trobada = False


#definició de llistes
lletres = ['A','B','C','D','E']
oculta = []
ll_entrada = []
ll_pistes = []
intents = []

print("Comença el joc de Python Mastermind")
print("Generant combinació oculta ...\n")

#guardo lletres a str per printar a input()
for lletra in lletres:
    lletres_str += lletra

#generar combinació oculta
#importo random
import random

#faig un random de lletra fins a posició MIDA
i = 0
for i in range(MIDA):
    #print(random.choice(lletres))
    lletra = random.choice(lletres)
    oculta.append(lletra)

#xivato
print("La combinació oculta és: ", end = "")
for lletra in oculta:
    print(lletra, end = "")

#mentre es tingui vides i no sigui trobada fes
while (vida < VIDES) and not trobada:
    
    #mostra vides
    print("\nVides restants:", VIDES - vida)
    
    #mostra intents i pistes, inicialment buida
    for intent in intents:
        print(intent)
    
    #mentre no tenim l'ok de validació, demana
    ok = False
    while not ok:
      #demana
      entrada = input("\nIntrodueix combinació de 4 lletres amb format " + lletres_str + " : ")
      #verica entrada
      #verica mida
      if len(entrada) == MIDA:
        #print("OK MIDA", MIDA)
        #verifica lletres permeses
        #reset variables
        i = 0
        conta = 0
        for i in range(MIDA):
                if entrada[i] in lletres:
                    #print("Lletra ", entrada[i], " és lletra permesa")
                    conta += 1
        if conta == MIDA:
            #print (MIDA, " lletres OK")
            ok = True
        #else:
            #print("NO LLETRES")
      #else:
        #print("NO MIDA")
    
    #print("OK CONTINUEM")
    
    #guarda entrada a llista
    ll_entrada.clear()
    for lletra in entrada:
        ll_entrada.append(lletra)
     
    #copio la llista oculta
    copia = oculta.copy()
    #print("Còpia:", copia)
    
    #inicialitzo
    ll_pistes.clear()
    pistes_ok = ""
    
    #miro pistes
    #faré 2 'passades' per l'entrada, perquè amb només 1 passada es marcaven incorrectament posicions
    #per tant 1r faig una 'passada' per mirar les lletres ok [#]
    #i les que no, les marco com a [-]
    i = 0
    for i in range(MIDA):
        #si la lletra HI ÉS, i està a la mateixa posició que la 'seqüència',
        #escriu '#' i la marquem com a trobada
        if entrada[i] == copia[i]:
            ll_pistes.insert(i, "#")
            #print(entrada[i], i, copia[i], i,  "#")
            copia[i] = "x" #marca com a OK comprovada
        else:
            ll_pistes.insert(i, "-")
            #print(entrada[i], i, "-")
    
    #miro pistes
    #faig una 2a 'passada' per mirar les lletres que estan a posicions incorrectes
    #només les marco amb [*] si estan a copia i no tenen marca [#]
    #així 'actualitzo' algunes marques [-] escrites a la 1a 'passada'
    i = 0
    for i in range(MIDA):
        #si la lletra HI ÉS, però NO està a la mateixa posició que la 'seqüència',
        #escriu '*' i la marquem com a trobada
        #per buscar la posició fem servir .index, que retorna l'index (posició) d'un valor donat
        #retorna l'index del 1r element que trobi
        if entrada[i] in copia and ll_pistes[i] != "#":
            #print(copia.index(entrada[i]))
            #print(copia[copia.index(entrada[i])])
            copia[copia.index(entrada[i])] = "x"
            #ll_pop.(i)
            #ll_pistes.insert(i, "*")
            ll_pistes[i] = "*"
    
    print("\nXivatos:")
    print(oculta)
    print(copia)
    print(ll_entrada)
    print (ll_pistes)
    
    #guardo pistes amb espais
    for pista in ll_pistes:
        pistes_ok += pista + " "
    
    #llista intents
    intents.append(entrada + " => " + pistes_ok)
    
    #trobada ?
    if pistes_ok == TROBADA:
        trobada = True
        print("\nUAU enhorabona! Ets un geni !!!")
    
    #consumim vida
    vida += 1
    

    

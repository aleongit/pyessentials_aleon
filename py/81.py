# -*- coding: utf-8 -*-
#Aleix Leon

#Set
#7 exercicis amb menú

# -----------------------------------------------------------------------

#declaració

exercicis =["Sortir",\
            "Afegir una llista d'elements a un conjunt",\
            "Retornar un conjunt d'elements repetits",\
            "Conjunt nou amb duplicats eliminats",\
            "Actualitzar el 1r conjunt amb elements que només existeixen al 1r conjunt i no al 2n conjunt",\
            "Treure 10, 20, 30 elements d'un conjunt alhora",\
            "Cadena amb caràcters únics",\
            "Textos de Josep Carner i Manuel de Pedrolo"]
opcio = 1
#menú opcions amb 0 per sortir
while (opcio != 0):

    print("\nSet - Conjunts")
    
    #mostro a usuari opcions i (posició + 1)
    for i in range(len(exercicis)):
        print("[Opció " + str(i) + "]", exercicis[i])
    #demano opció
    opcio = int( input("\nQuin exercici vols veure ? [1-7] : "))

    print("\nExercici",opcio)
    
    if opcio == 1:
        sampleSet = {"Yellow", "Orange", "Black"}
        sampleList = ["Blue", "Green", "Red"]
        
        #per afegir més d'1 valor es fa servir .update
        sampleSet.update(sampleList)
        print(sampleSet)

    elif opcio == 2:
        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}
        
        print("Mètode &")
        print(set1 & set2)

        print("\nMètode .intersection")
        inter = set1.intersection(set2)
        print(inter)
        
    elif opcio == 3:
        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}
        
        print("Mètode convertint a llista els dos conjunts")
        #converteixo i unifico els dos conjunts a llista, i en faig el conjunt
        set3 = set(list(set1)+list(set2))
        print(set3)
        
        print("\nMètode | o union")
        print(set1 | set2)
        set4 = set1.union(set2)
        print(set4)

    elif opcio == 4:
        set1 = {10, 20, 30}
        set2 = {20, 40, 50}
        
        print("Mètode diferència")
        print(set1 - set2)
        set3 = set1.difference(set2)
        print(set3)
    
    elif opcio == 5:
        set1 = {10, 20, 30, 40, 50}
        print("Mètode diferència")
        print(set1 - {10,20,30})
        set3 = set1.difference({10,20,30})
        print(set3)

    elif opcio == 6:
        
        cadena = 0
        while (cadena != "0"):
            cadena = input("\nIntrodueix string [0 Sortir]: ")
            
            #converteixo la cadena a set i comparo longitud
            setCadena = set(cadena)
            if len(setCadena) == len(cadena):
                print(f"{cadena} => té caràcters únics")
            else:
                print(f"{cadena} => té duplicats")
                
    elif opcio == 7:
    
        TEXT1 = "Com les maduixes Menja maduixes l’àvia d’abans de Sant Joan; per més frescor, les vol collides d’un infant. Per això la néta més petita, que és Pandara, sabeu, la que s’encanta davant d’una claror i va creixent tranquil·la i en ‘admiració i a voltes, cluca d’ulls, aixeca al cel la cara, ella, que encar no diu paraules ben ardides i que en barreja en una música els sentits, cull ara les maduixes arrupides, tintat de rosa el capciró dels dits. Les prunes d’or Aglaia té una set que eixuga el seny, la parla… Superbament s’aixeca, damnant el seu descans, i enfonsa en la prunera les cobejoses mans i enlaira tot el rostre, com si volgués besar-la. I l’arbre, que amb un lleu serpejament de branques sembla oferir-nos l’or, la mel d’algun pecat, s’estremeix un moment de la ferocitat del gran perfum impúdic i de les dents tan blanques. XVI Els codonys tardorals Però ja saps com elles es tornen malgirbades  per fills i feines, o perquè no n’han tingut, i amb cara tediosa caminen desmarxades i són codonys, diries, el fruit més boterut—. I l’altre amic que deia: —Quan fina tot esclat, nosaltres rondinem, esgarriant les passes, i flagel·lem el dia amb folles amenaces, saturns a la memòria del goig mal escampat. Llavores, el codony, que es féu vell en la branca,  dins el calaix perfuma la nostra roba blanca, i si l’amorosim al caliu de la llar i l’acostem als llavis sorruts, és dolç, encar."
        TEXT2 = "Ho havia planificat tot durant 20 anys. S’havia desfet de tot i de tothom. Estava segur que, en aquells moments, ja no el coneixia ningú. No quedava cap fotografia amb el seu veritable físic. I havia tingut tantes identitats diferents que ni ell es recordava de totes. Ara havia decidit començar una nova vida en un lloc on no el coneixia ningú. Era un poble qualsevol que un dia va veure mentre feia un viatge. Havia pensat que seria un bon lloc per començar de zero. El trajecte era la part més difícil. A l’estació va comprar un bitllet de tren nocturn amb destinació a Manchester. No volia que el busquessin enlloc. Baixaria al poble que havia triat abans d’arribar a la ciutat. També s’havia preocupat pel físic: ara duia bigoti i inflava les galtes d’una manera que li canviava la cara. Dret al passadís va esperar la sortida del tren. I va encendre l’última cigarreta, perquè a la nova vida pensava desfer-se d’aquest costum. El tabac li va semblar més bo que altres vegades i va fumar lentament, per fer durar el plaer." 
        
        signes =",.;"
        
        #print(TEXT1)
        #print(TEXT2)
        
        #Elimina en ambdues variables els signes de puntuació (,.;) i transforma a minúscules (mètode lower).
        
        #amb list comprehension - "".join : passo llista a string
        #agafo cada lletra de la llista que no estigui a 'signes' i ahora converteixo a mínuscules
        TEXT1 = "".join([str(el).lower() for el in TEXT1 if el not in signes])
        TEXT2 = "".join([str(el).lower() for el in TEXT2 if el not in signes])
        
        #print(TEXT1)
        #print(TEXT2)
        
        #Quantes paraules té TEXT1 ? i Quantes TEX2?
        
        #amb list comprehension extrec les paraules amb .split i les conto amb len()
        M1 = len([paraula for paraula in TEXT1.split()])
        M2 = len([paraula for paraula in TEXT2.split()])
        print(f"TEXT1 té {M1} paraules")
        print(f"TEXT2 té {M2} paraules")
        
        #Quines paraules té TEXT1 que continguin 2 lletres ‘a’  que també té TEXT2?
        
        #amb list comprehension creo conjunts de paraules i que tenen mínim 2 'a'
        p1 = set([paraula for paraula in TEXT1.split() if paraula.count('a')>=2])
        p2 = set([paraula for paraula in TEXT2.split() if paraula.count('a')>=2])
        #print("\n",p1)
        #print("\n",p2)
        #amb intersecció dels dos conjunts (&) trobo les paraules amb comú
        print(f"\n{p1 & p2} paraules que estan a TEXT1 i TEXT2 amb 2 'a'")
        
        #Quines paraules hi ha AMB ACCENT que estan en ambdós variables TEXT1 i TEXT2?
        
        accents = "àèéíòóú"
        #amb un for trec les paraules, i amb l'altre miro la lletra de cada paraula si té accent per incloure-la
        p1 = set([paraula for paraula in TEXT1.split() for lletra in paraula if lletra in accents])
        p2 = set([paraula for paraula in TEXT2.split() for lletra in paraula if lletra in accents])
        #print("\n",p1)
        #print("\n",p2)
        print(f"\n{p1 & p2} paraules que estan a TEXT1 i TEXT2 amb accents")
        
        #Quines paraules que contenen un apòstrof, un guió o bé un punt volat (·) estan a TEXT1 i no a TEXT2?
        
        signes = "’-·"
        #amb un for trec les paraules, i amb l'altre miro la lletra de cada paraula si té símbol per incloure-la
        p1 = set([paraula for paraula in TEXT1.split() for lletra in paraula if lletra in signes])
        p2 = set([paraula for paraula in TEXT2.split() for lletra in paraula if lletra in signes])
        #print("\n",p1)
        #print("\n",p2)
        print(f"\n{p1 - p2} paraules que estan a TEXT1 i no a TEXT2 amb signes")
        
        #Quines paraules que tenen almenys 4 vocals hi ha TEXT1 o TEX2 però no comparteixen?
        vocals = "aeiouàèéíòóú"
        #amb un for separo les paraules i selecciono les que tenen mida >=4 després de la intersecció entre paraula i vocals
        #(cal convertir a set els strings)
        p1 = set([paraula for paraula in TEXT1.split() if (len(set(paraula).intersection(set(vocals))) >= 4)])
        p2 = set([paraula for paraula in TEXT2.split() if (len(set(paraula).intersection(set(vocals))) >= 4)])
        #print("\n",p1)
        #print("\n",p2)
        print(f"\n{p1 ^ p2} paraules que estan a TEXT1 i a TEXT2 (no comunes) amb almenys 4 vocals")
        
    else:
        print("Opció incorrecte")

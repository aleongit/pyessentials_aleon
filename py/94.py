#Aleix Leon
#Diccionaris

#Funcionalitats: Afegir Alumne, Eliminar alumne, Afegir  notes a alumne (mòdul, nota),
# llistat de tots els alumnes (la llista de tots els alumnes),
# llistat d’un alumne (el nom de l’alumne i totes les seves notes),
# estadístiques (que responen a les qüestions més avall) i sortir.

#Demana els noms dels alumnes per teclat, els noms dels alumnes d'una classe i les notes que han obtingut.
#Cada alumne pot tenir diferent quantitat de notes, que també  s’introduiran per teclat,
# valida que siguin notes entre 0 i 10.
#Guarda la informació en un diccionari, les claus seran els noms dels alumnes i els valors seran llistes de tuples
#de  parelles de tuples  (modul, nota) per emmagatzemar les notes de cada alumne. 

import random

#declaració llistes per carregar valors
alumnes = ["Jose","Marc","Clàudia","Jordi","Xavi"]
moduls  = [(1,"M1"),(2,"M2"),(3,"M3"),(4,"M4"),(12,"M12"),(13,"M13")] #llista de tuples

novalid ="0123456789<>{}[]?¿!¡+*/\$%&= "

#diccionari taula notes
dNotes = { 0:("Suspès","Molt Deficient"),1:("Suspès","Deficient"),2:("Suspès","Deficient"),\
           3:("Suspès","Insuficient"),4:("Suspès","Insuficient"),5:("Aprovat","Suficient"),\
           6:("Aprovat","Bé"),7:("Aprovat","Notable"),8:("Aprovat","Notable"),\
           9:("Aprovat","Excel·lent"),10:("Aprovat","Excel·lent")}

#diccionari classe amb random notes
#amb clau de llista alumnes, amb llista de tuples (mòdul,nota)
dClasse = {el : [(el2[0],random.randint(0,10)) for el2 in moduls] for el in alumnes }

for el in dClasse:
    print(el,dClasse[el])
#print(type(dClasse["Jose"]))

#diccionari menú opcions
dMenu = {1:"1. Afegir Alumne",\
         2:"2. Eliminar Alumne",\
         3:"3. Afegir Notes a Alumne",\
         4:"4. Llistat Alumnes",\
         5:"5. Llistat d'1 Alumne",\
         6:"6. Estadístiques",\
         7:"7. Sortir"}
op = 0
while op != 7:
    
    try:
        #obting claus (noms alumnes)
        kAlumnes = dClasse.keys()
        #print("claus: ",kAlumnes,"\n")
        print()
        for el in dMenu:
            print(dMenu[el])
        op = int(input("\nIntrodueix una opció: "))
        
        #control opció
        if op > 7 or op <= 0:
            print("\nOpció incorrecte")
    
    #control tipus valor
    except ValueError:
        print("\nValor incorrecte")
        
    if op == 1:
        #print("opcio 1")
        print(dMenu[op])
        
        #ves demananant fins l'ok de nou alumne afegit
        ok = False
        #print(nom)
        while ok == False:
            nom = input("\nIntrodueix el nom d'un alumne: ")
            #si existeix, missatge error
            if nom in kAlumnes:
                print("\n** FATAL ERROR >> Alumne in system **")
            elif nom == "" or nom in novalid:
                print("Nom no vàlid")
            else:
                #si no existeix, afageix a diccionari amb llista buida
                dClasse[nom] = []
                ok = True
                print(kAlumnes)       
        
    if op == 2:
        print(dMenu[op])
        
        nom = ""
        torna = False #control tornar enrere
        print(nom)
        while nom not in kAlumnes and torna == False:
            print("\n",kAlumnes)
            nom = input("\nIntrodueix nom del alumne a eliminar [0 = Tornar]: ")
            #per tornar enrere
            if nom == "0":
                torna = True
            #si no existeix, missatge error
            elif nom not in kAlumnes:
                print("\n** FATAL ERROR >> Alumne NOT in system **")
            else:
                #elimino alumne amb .pop
                dClasse.pop(nom)
        
        print(kAlumnes)   
        
    if op == 3:
        print(dMenu[op])
        
        nom = ""
        #print(nom)
        if len(dClasse) == 0:
            print("No hi ha alumnes")
            
        else:
            while nom not in kAlumnes:
                print("\n",kAlumnes)
                nom = input("\nIntrodueix el nom d'un alumne: ")
                #si existeix, missatge error
                if nom not in kAlumnes:
                    print("\n** FATAL ERROR >> Alumne NOT in system **")
            #mòduls
            modul = 1
            while modul != 0:
                print(dClasse[nom])
            
                try:
                    modul = int(input(f"\nIntrodueix Mòdul:{[el[0] for el in moduls]} [0 = Exit]: "))
                    #control mòduls, miro en una llista per cada element[0] de la tupla moduls
                    if modul not in [el[0] for el in moduls]:
                        print("\nMòdul erroni")
                    #control tipus valor
                except ValueError:
                    print("\nValor incorrecte")
                    modul =""
                #si el mòdul existeix
                if modul in [el[0] for el in moduls]:
                    nota =-1
                    #control nota
                    while (nota > 10) or (nota < 0):
                        try:
                            nota = int(input(f"\nIntrodueix nota pel mòdul {modul} [0-10]: "))
                            if (nota > 10) or (nota < 0):
                                print("Nota incorrecta")
                        #control valor
                        except ValueError:
                            print("Valor incorrecte")
                        else:
                            #afageixo/modifico tupla a llista de diccionari
                            #nova tupla
                            tNotaCicle = (modul,nota)
                            #print("element diccionari: ", dClasse[nom])
                            #print("element llista: ", dClasse[nom][0])
                            #print("1r element tupla dins llista: ",dClasse[nom][0][0])
                    
                            #busco si ja té nota per mòdul a 1a posició tupla, per cada element de llista
                            #si existeix, substitueix tupla
                            existeix = False
                            for i in range(len(dClasse[nom])):
                                if dClasse[nom][i][0] == modul:
                                    dClasse[nom][i] = tNotaCicle
                                    existeix = True             
                            #si no hi és, afageix tupla com element llista dins diccionari
                            if not existeix:
                                dClasse[nom].append(tNotaCicle) 
    
    if op == 4:
        print(dMenu[op],"\n")
        for el in kAlumnes:
            print("* - ",el)
    
    if op == 5:
        print(dMenu[op])
        
        nom = ""
        print(nom)
        if len(dClasse) == 0:
            print("No hi ha alumnes")
        else:
            while nom not in kAlumnes:
                print("\n",kAlumnes)
                nom = input("\nIntrodueix el nom d'un alumne: ")
                #si existeix, missatge error
                if nom not in kAlumnes:
                    print("\n** FATAL ERROR >> Alumne NOT in system **")
            
            #control si no té notes
            if len(dClasse[nom]) == 0:
                print(f"\n{nom} no té notes")
                
            else:
                #llisto notes
                notesAlumne= [] #llista notes individuals
                aprovats = 0
                #per cada d'alumne mostro element llista, i element tuples dins llista
                # i afageixo notes en nova llista per càlcul mitjana
                # també acumulo quantitat aprovats
                for el in dClasse[nom]:
                    print(f"La nota del mòdul M{el[0]} és {el[1]} => {dNotes[el[1]][0]} amb {dNotes[el[1]][1]}")
                    notesAlumne.append(el[1])
                    if el[1] >= 5:
                        aprovats += 1
                #càlculs individuals
                
                #mitjana alumne
                print("\nNota mitja", round((sum(notesAlumne)/len(notesAlumne)),2))
                
                #quantitat aprovats i suspesos
                if aprovats == len(dClasse[nom]):
                    print("\nEnhorabona! tot aprovat!")
                else:
                    print(f"{nom} ha aprovat {aprovats} i ha suspès {len(dClasse[nom]) - aprovats}")
                    
    if op == 6:
        print(dMenu[op])
        
        if len(dClasse) == 0:
            print("No hi ha alumnes, no hi ha estadístiques")
        
        else:
            #declaro
            totaprovat = []
            tres = []
            dMitjana = {}
            llMitjana = []
            
            #per cada alumne, conto aprovats i acumulo per mitjana
            for el in kAlumnes:
                aprovats = 0
                suma = 0
                print(el)
                #recorro les notes de cada alumne (cada element diccionari = llista de tuples)
                for i in range(len(dClasse[el])):
                    #comprovo nota a posició 1 de la tupla
                    if dClasse[el][i][1] >= 5:
                        aprovats += 1
                    suma += dClasse[el][i][1]
                #si la q d'aprovats és el total de notes "tot aprovat"
                if aprovats == len(dClasse[el]):
                    totaprovat.append(el)
                #sinó miro si n'ha suspès 3, i afageixo a llista a part
                elif (len(dClasse[el]) - aprovats) == 3:
                    tres.append(el)
                    
                #afageixo nota mitja
                #per mitjana creo diccionari amb clau alumne i nota mitjana
                #també creo llista de mitjana per càlcul
                
                #control si no té notes, posa un 0
                if len(dClasse[el]) == 0:
                    dMitjana[el] = 0
                    llMitjana.append(0)
                else:
                    dMitjana[el] = round(suma/len(dClasse[el]),2)
                    llMitjana.append(round(suma/len(dClasse[el]),2))

            #creo llista dels millors per si més d'un alumne coincideix amb la nota max de mitjana
            millors = [el for el in dMitjana if dMitjana[el] == max(llMitjana)]
            
            print(totaprovat)
            print(tres)
            print(dMitjana)
            print(llMitjana)
            print(millors)
 
            print("\nAlumnes que ho han aprovat tot:", len(totaprovat))
            print("Alumnes amb 3 suspesos:", len(tres))
            print(f"Alumne amb millor mitjana és/són {millors} amb nota mitja de {max(llMitjana)}")
                    
    if op == 7:
        print(dMenu[op])
        print("\nAdéu! Que tinguis un bon dia")

        
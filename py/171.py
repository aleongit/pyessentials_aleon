#Aleix Leon

import sys

linies = []
#fitxer = "song.txt"
fitxer_out = "sortida.txt"
sortida = ""
arg = ""
H ="--help"
PARAMETRES = ["-i","-p","-P","-w","-f"]
i = False
p = False
P = False
w = False
f = False

#4
#$python3 ex4.py file [c] [-i -p -w -f] [--help]

#1. ex4.py: Escriviu un programa per comptar el nombre de línies d'un fitxer text que passeu com a 1r argument.

#2. Afegiu un segon argument opcional c que compta les línies que contenen el caràcter c.

#3. Si s’especifica l’argument opcional -i, el comportament és al contrari,
#compta totes les línies que no contenen el caràcter c.

#4. Afegiu al programa anterior l’argument opcional -p, que farà que compti les línies de l’arxiu
#que comencen pel caràcter c. Recordeu que si s’especifica -i farà el contrari.

#5. Si en comptes d’una p minúscula és una P majúscula, és fixarà en l’últim caràcter de la línia
#(compte amb el “\n” final de línia que no considerem últim caràcter en aquest cas).

#6. Si a més hi ha l’argument opcional -w comptarà, a part de les línies, les paraules
#que contenen el caràcter c. Si no s’especifica c haurà de comptar totes les paraules.
#Recordeu que si hi ha -i el comportament és al contrari i -P mira l’últim caràcter.

#7. Si també hi ha l’argument opcional -f la sortida no serà per pantalla,
#sinó a un arxiu anomenat sortida.txt

#8. Si només hi ha un argument i és --help mostrarà una pantalla d’ajuda on s’expliqui
#la funcionalitat de cada argument i mostri alguns exemples

#9. En cas que la combinació d’arguments no sigui correcta haurà de mostrar el missatge d’error .
#corresponent i mostrar la pantalla d’ajuda.

#10. Si no s’especifica cap argument cal que mostri un missatge d’error
#i indiqui quina és la comanda per obtenir ajuda.

def llegeixFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        ll = f.readlines()
    return ll

def comptaLinies(ll):
    return str(len(ll)) + f" línies\n"

def comptaLiniesC(ll,c,i=False):
    #print(*ll,end="\n")
    missatge = ""
    if not i:
        ll = [linia for linia in linies if c in linia]
        missatge = f" línies amb {c}\n"
    else:
        ll = [linia for linia in linies if c not in linia]
        missatge = f" línies sense {c}\n"
    #print(*ll,end="\n")
    return str(len(ll)) + missatge

def comptaLiniesCP(ll,c,i=False,p=False):
    missatge = ""
    if not p:
        pos = 0
        missatge += f" línies que comencen "
    else:
        pos = -2
        missatge += f" línies que acaben "
    if not i:
        # si linia és més gran que 1 (perquè no miri salts de línia)
        ll = [linia for linia in linies if len(linia) > 1 if c in linia[pos]]
        missatge += f"amb {c}\n"
    else:
        #no conta les línies amb salt de pàgina
        ll = [linia for linia in linies if len(linia) > 1 if c not in linia[pos]]
        #llista per salts de pàgina
        ll1 = [linia for linia in linies if len(linia) == 1]
        #extenc les dues llistes perquè sinó no tenia línies amb intro
        ll.extend(ll1)
        missatge += f"sense {c}\n"
    #print(*ll,end="\n")
    return str(len(ll)) + missatge

def comptaParaules(ll,c,i=False):
    missatge = ""
    #[word for sentence in text for word in sentence]
    if not i:
        ll = [paraula for linia in linies for paraula in linia.split() if c in paraula]
        missatge += f" paraules amb {c}\n"
    else:
        ll = [paraula for linia in linies for paraula in linia.split() if c not in paraula]
        missatge += f" paraules sense {c}\n"
    
    #cas c="" (totes les paraules)
    if c == "":
        missatge = " paraules totals\n"
    #print(*ll,end="\n")
    return str(len(ll)) + missatge

def comptaParaulesP(ll,c,i=False,p=False):
    missatge = ""
    if not p:
        pos = 0
        missatge += f" paraules que comencen "
    else:
        pos = -1
        missatge += f" paraules que acaben "
    #[word for sentence in text for word in sentence]
    if not i:
        ll = [paraula for linia in linies for paraula in linia.split() if c in paraula[pos]]
        missatge += f"amb {c}\n"
    else:
        ll = [paraula for linia in linies for paraula in linia.split() if c not in paraula[pos]]
        missatge += f"sense {c}\n"
    #print(*ll,end="\n")
    return str(len(ll)) + missatge

#imprimeix pantalla o fitxer
def imprimeix(f=False):
    #print(fitxer_out)
    if not f:
        print(sortida)
    else:
        with open(fitxer_out, "w", encoding="utf8") as f:
            f.writelines(sortida)
        print(f"sortida generada a {fitxer_out}")

def ajuda():
    print("#$python3 fitxer.py fitxerTXT [c] [-i -p -w -f] [--help]")
    print("                               c = caràcter")
    print("Per defecte sortida per pantalla / [-f] Sortida per fitxer")
    print("fitxer.py fitxer [-f]               --> línies")
    print("fitxer.py fitxer -w [-f]            --> línies + paraules")
    print("fitxer.py fitxer  c [-f]            --> linies amb c")
    print("fitxer.py fitxer  c -i   [-f]       --> linies sense c")
    print("fitxer.py fitxer  c -p/P [-f]       --> linies amb c -p principi/ -P final")
    print("fitxer.py fitxer  c -w   [-f]       --> linies + paraules amb c")
    print("fitxer.py fitxer  c -i -w   [-f]    --> linies + paraules sense c")
    print("fitxer.py fitxer  c -i -p/P [-f]    --> linies sense c -p principi/ -P final")
    print("fitxer.py fitxer  c -p/P -w [-f]    --> linies + paraules amb c -p principi/ -P final")
    print("fitxer.py fitxer  c -i -p/P -w [-f] --> linies + paraules sense c -p principi/ -P final")
               
def parametresRepetits(ll):
    #transformo tots els paràmetres a minúscules
    llr = [el.lower() for el in ll]
    #print(llr)
    #fa llista amb repetits, si 0 cap repetit
    return len([el for el in llr if llr.count(el)>1]) > 0

try:
    #print(sys.argv)
    #guardo comanda per sortida
    sortida += " ".join(el for el in sys.argv)+"\n"
    #trec 1r arg = nom, que molesta
    sys.argv.pop(0)
    #print(sys.argv)
    #mida arguments
    n = len(sys.argv)
    
    #mirem si 0 arguments
    if n == 0:
        print("*FATAL ERROR* cap argument")
        print("escriu --help per ajuda")
    
    #mirem si 1 argument
    elif n == 1:
        arg = sys.argv[0]
        #si argument és ajuda
        if arg == H:
            ajuda()
        #considerem arg fitxer, si no existeix fitxer error except
        #cas només línies
        else:
            fitxer = arg
            sortida += comptaLinies(llegeixFitxer(fitxer))
            imprimeix()
    elif n > 1 and n <= 6:
        #comprovem 1r agument, sinó és fitxer except
        fitxer = sys.argv[0]
        linies = llegeixFitxer(fitxer)
        #comprovem 2n argument
        arg = sys.argv[1]
        #mirem si és c (caràcter) = mida 1 considerem caràcter
        if len(arg) == 1:
            #print("és caràcter")
            #si és caràcter només paràmetre (fitxer + caràcter)
            if n == 2:
                #cas comptar línies caràcter
                sortida += comptaLiniesC(linies,arg)
                imprimeix()
            #si en té més, seran paràmetres (fitxer + c + 4 possibles paràmetres)
            else:
                #caràcter
                c = arg
                #revisem paràmetres
                param = sys.argv[2:]
                #comprovem si tots els paràmetres són vàlids
                if all([el in PARAMETRES for el in param]):
                    #print("tots vàlids")
                    #comprovem si vàlids passats més d'1 cop (repetits)
                    #print(parametresRepetits(param))
                    if not parametresRepetits(param):
                        #print("ok cap repetit")
                        #mirem paràmetres
                        if "-w" in param:
                            w = True
                        if "-p" in param:
                            p = True
                        if "-P" in param:
                            P = True
                        if "-i" in param:
                            i = True
                        #segons paràmetres
                        if p and not w:
                            #p
                            sortida += comptaLiniesCP(linies,c,i,False)
                        elif P and not w:
                            #P
                            sortida += comptaLiniesCP(linies,c,i,True)
                        elif w and not p and not P:
                            #w
                            sortida += comptaLiniesC(linies,c,i)
                            sortida += comptaParaules(linies,c,i)
                        elif w and p:
                            #w + p
                            sortida += comptaLiniesCP(linies,c,i,False)
                            sortida += comptaParaulesP(linies,c,i,False)
                        elif w and P:
                            #w + P
                            sortida += comptaLiniesCP(linies,c,i,True)
                            sortida += comptaParaulesP(linies,c,i,True)
                        elif not p and not P and not w:
                            sortida += comptaLiniesC(linies,c,i)
                        #cas -f
                        if not "-f" in param:
                            imprimeix()
                        else:
                            imprimeix(True)
                    else:
                        print(f"*FATAL ERROR* algun paràmetre repetit\n")
                        ajuda()
                else:
                    print(f"*FATAL ERROR* algun paràmetre no vàlid\n")
                    ajuda()
        #sinó és c, pot ser paràmetre -w o -f
        elif arg in PARAMETRES:
            #print("ok és un paràmetre")
            #si 2 arguments i -w
            if n == 2 and arg == "-w":
                #cas comptar línies + paraules
                sortida += comptaLinies(linies)
                sortida += comptaParaules(linies,'')
                imprimeix()
            #si 2 arguments i -f
            elif n == 2 and arg == "-f":
                #cas només comptar línies + sortida impressora
                sortida += comptaLinies(linies)
                imprimeix(f=True)
            else:
                print(f"*FATAL ERROR* paràmetre no permès a aquí\n")
                ajuda()
        else:
            print(f"*FATAL ERROR* {arg} no és caràcter o paràmetre vàlid\n")
            ajuda()
    else:
        print("*FATAL ERROR* massa paràmetres")
        ajuda()
#si error IO
except IOError:
    print(f"*FATAL ERROR* {fitxer} no existeix\n")
    ajuda()

finally:
    pass
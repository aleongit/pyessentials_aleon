#Aleix Leon

#3-2
#Donada la primera estrofa de "The fly song": 
#Una mosca volava per la llum
#i la llum es va apagar
#i la pobre mosca va quedar a les fosques
#i la pobre mosca no va poder volar. 

#Crea un programa que escriu el fitxer the_fly_song.txt:
#Per crear la cançó cal escriure la primera estrofa.
#La segona estrofa és igual a la primera estrofa, però canviant les vocals per a. 
#La tercera estrofa és igual a la primera estrofa, però canviant les vocals per e, ...etc...

#Feu la funció retorna_substitucio(linia, una_vocal), que retorna una linia amb les vocals canviades per una_vocal.

fitxer ="song.txt"
vocals ="aeiou"

estrofa = ["Una mosca volava per la llum\n","i la llum es va apagar\n","i la pobre mosca va quedar a les fosques\n","i la pobre mosca no va poder volar.\n\n"]

def printFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

#retorna string generat d'una llista on afageix vocal passada si és vocal, i sinó la lletra
def retorna_substitucio(linia, vocal):
    return "".join([vocal if el in vocals else el for el in linia])

try:
    #obrim fitxer w i tanquem
    with open(fitxer, "w", encoding="utf8") as f:
        #escrivim 1a estrofa
        f.writelines(estrofa)
        #per cada vocal, canvia les línies d'estrofa i escriu a fitxer
        for v in vocals:
            for l in estrofa:
                f.write(retorna_substitucio(l,v))
    printFitxer(fitxer)
    
#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass


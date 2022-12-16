#Aleix Leon

#3-4
#Crea un fitxer de text abece.txt, en python amb el contingut: 
#a
#bb
#ccc
#dddd
#...
#zzzzzzzzz...zz

#utilitzarem una trampeta
#lletra="a"
#lletraSeguent=chr(ord(lletra)+1)

import string
abc = string.ascii_lowercase

fitxer = "abece.txt"

def printFitxer(fitxer):
    with open(fitxer, "r", encoding="utf8") as f:
        print(f.read())

#versió Aleix
def liniesLletres():
    return [abc[i]*(i+1)+"\n" for i in range(len(abc))]

#versió trampeta enunciat
#sense string lletres, fins z
#variable multiplicadora que incrementa a la següent lletra
def trampeta():
    q = 1
    cadena = ""
    lletra = "a"
    while lletra <= 'z':
        cadena += lletra*q + "\n"
        lletra = chr(ord(lletra)+1)
        q += 1
    return cadena

try:
    #obrim fitxer w i tanquem
    with open(fitxer, "w", encoding="utf8") as f:
        #versió Aleix
        f.writelines(liniesLletres())
        #versió trampeta
        f.write(trampeta())
    printFitxer(fitxer)
    
#si error IO
except IOError:
    print("el fitxer no existeix")
finally:
    pass


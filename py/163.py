#Aleix Leon

#3
#Fes un programa que afegeixi una línia més al fitxer de text "text.txt" i el mostri per pantalla.
#Fes-lo usant les comandes open i close.
#Per poder afegir al fitxer cal obrir-lo en mode append i després per mostrar-lo
#cal tornar-lo a obrir en mode read

import sys

linia = "Línia nova\n"

#provem
try:
    #fitxer mode append
    f = open("text.txt", "a", encoding="utf8")
    #afegim línia
    f.writelines(linia)
    #tanquem
    f.close()
    #tornem a obrir en mode lectura
    f = open("text.txt", "r", encoding="utf8")
    print(f.read())
    #per provar altres errors
    #raise KeyError(message)
    #raise KeyboardInterrupt
#si error IO
except IOError:
    print("el fitxer no existeix")
#qualsevol altre error, mostrem error
except:
    print("oops",sys.exc_info()[0])
else:
    #tanquem fitxer
    f.close()
    #print("fitxer tancat")


#Aleix Leon

#2
#Fes un programa que llegeixi el fitxer de text "text.txt" anterior i el mostri per pantalla.
#Fes-lo usant les comandes open i close.

#provem
try:
    #fitxer mode lectura
    f = open("text.txt", "r", encoding="utf8")
    print(f.read())
#si error IO
except IOError:
    print("el fitxer no existeix")
else:
    #tanquem fitxer
    f.close()
    #print("fitxer tancat")


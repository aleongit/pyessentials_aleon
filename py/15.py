#donat un sting:
#mida > 10 caràcters
#mida < 10 caràcters i conté algún * + / -
#mida = 10 caràcters i comença per -
#mida = 10 caràcters i acaba per .

#demanar string
frase = input ("Introdueix una frase: ")

mida = len(frase)
print ("mida",mida)

if mida > 10:
    print("frase de + 10 caràcters")

elif mida < 10:
    print("frase de - 10 caràcters")
    
    #comprovar si caràcters * + / -
    if ('*') in frase:
        print("conté *")
    if ('+') in frase:
        print("conté +")
    if ('/') in frase:
        print("conté /")
    if ('-') in frase:
        print("conté -")
else:
    print("frase de 10 caràcters")
    #comprovar si comença per -
    if frase[0] == '-':
        print("la frase comença per -")
        #print (frase[0])
    #comprovar si acaba per .
    if frase[mida - 1] == '.':
        print("la frase acaba per .")
        #print (frase[mida - 1])
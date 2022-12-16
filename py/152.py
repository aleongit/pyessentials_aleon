#Aleix Leon

#Exercicis d’argument per línia de comandes

#2
# programa que accepta 2 arguments, el primer comprova que és un string,
#el segon comprova que són dígits i el transforma a sencer,
#i si és així fa un print de l’string tantes vegades com indica el paràmetre.
#Indica amb un print quin error ha comès l’usuari en cas que els arguments siguin incorrectes.

from module15 import *

#control número arguments
if  arg() == 0:
    print("Cap argument")
elif arg() == 1:
    print("Falta 1 argument")
elif arg() == 2:
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    
    #comprovar arguments  
    #l'argument sempre serà tipus string
    #però suposem només lletres sense dígits
    if not nomes_lletres(treu_accents(a1)) or not nomes_digits(a2):
        if not nomes_lletres(a1):
            print(f"L'argument 1: {a1} >> ha de tenir només lletres")
        if not nomes_digits(a2):
            print(f"L'argument 2: {a2} >> ha de tenir només dígits")
    else:
        print((a1+"\n")*int(a2))
else:
    print("T'has passat d'arguments")
#Aleix Leon
#endevinar nombre entre 1 i 9
#demanar número fins que s'encerti (amb while)

#funció random
import random

#calculo num random
num_r = random.randint(1, 9)
print (num_r)

#inicialitzo num a 0 per entrar al bucle (trampeta)
num = 0
while num_r != num:

    #demano número
    num = int(input ("Introdueix un número de 1 al 9: "))

    if (num < 1) or (num > 9):
        print("No has entrat un número del 1 al 9:")
    else:
        #print("Número OK")
        #abs per tenir número absolut (sense símbol)
        dif = abs(num - num_r)
        print("dif:", dif)
        
        if dif == 0:
            print("ENHORABONA! Ets un crack")
        elif dif == 1:
            print("Quasi! Pels pèls")
        elif dif > 4:
            print("Dedica't al parxís")
        else:
            print("La propera vegada ho faràs millor")
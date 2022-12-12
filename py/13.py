#endevinar nombre entre 1 i 9

#funció random
import random

#calculo num random
num_r = random.randint(1, 9)
print (num_r)

#demano número
num = int(input ("Introdueix un número de 1 al 9: "))

if (num < 1) or (num > 9):
    print("No has entrat un número del 1 al 9:\nAdéu")
else:
    #print("Número OK")
    #càlculs
    dif = abs(num - num_r)
    print(dif)
    
    if dif == 0:
        print("ENHORABONA! Ets un crack")
    elif dif == 1:
        print("Quasi! Pels pèls")
    elif dif > 4:
        print("Dedica't al parxís")
    else:
        print("La propera vegada ho faràs millor")

    
    
    
    
     

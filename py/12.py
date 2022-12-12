#múltiple de 7 i múltiple de 5.

#forço l'entrada a enter
num = int(float(input ("Introdueix un número enter: ")))

if (num % 5 == 0) and (num % 7 == 0):
    print(num, "és múltiple de 5 i de 7")
else:
    if (num % 5 == 0):
        print(num, "és múltiple de 5")
    elif (num % 7 == 0):
        print(num, "és multiple de 7")
    else:
        print(num, "NO és multiple ni de 5 ni de 7")
#Aleix Leon
#Repàs

#Fes un bucle que demani un nombre enter 
#Surt del bucle quan l’usuari entri un enter entre 1 i 20 per teclat

#Calcula el resultat de la fórmula n·(n+1) / 2. 
#Compte: el resultat de la fórmula ha de ser enter

#Imprimeix per pantalla el resultat anterior

#Fes un bucle que sumi els enters des d’1 fins al nombre entrat per teclat
#Compara el resultat de la fórmula amb la suma calculada en el bucle
#Si són iguals escriu “Carl Friedrich Gauss tenia raó”
#Sinó escriu “Alguna cosa ha fallat”

ok = False
n = 0
while not ok:
    try:
        n = int(input("\nIntrodueix nombre enter [1-20]: "))
        
    except ValueError:
        print("\nNo és un nombre enter")

    else:
        if n < 1 or n > 20:
            print("\nNombre ha de ser de 1 a 20")
        
        else:            
            ok = True
        
#print("ok")
#càlcul n·(n+1) / 2

calcul = int((n * (n+1) ) / 2)
print(calcul,type(calcul))

llEnters = [i for i in range(1,n+1)]
ll = [str(i) for i in llEnters]

#amb .join cal que els elements de llista siguin iterables (strings)
#cal passar l'enter a string
print(" + ".join(ll),"= ", sum(llEnters))

if calcul == sum(llEnters):
    print("Carl Friedrich Gauss tenia raó")
else:
    print("Alguna cosa ha fallat")

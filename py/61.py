#Aleix Leon

#List Comprehension
#10 exercicis amb menú

# 1.Crear una llista idèntica a llistaExemple mitjançant la comprensió de la llista.
# llistaExemple=[1,2,3,4,5,6]

# 2.Crear una llista a partir dels elements d'un interval de 1200 a 1980 ambdós inclosos,
# amb passos de 130, mitjançant la comprensió de la llista.

# 3.Crear una llista nova a partir de l’anterior, però sumeu 6 a cada element.

# 4.Crear una llista que sigui els quadrats de cada element de la llista.
# llistaExemple=[1,2,3,4,5,6]

# 5.Crear una llista a partir dels quadrats de cada element de la llista si el quadrat > 50.
# llistaExemple2=[1,2,3,7,9,10]

# 6.Crear una llista amb tots els números de l’1 al 1000 que són divisibles per 7.

# 7.Crear una llista amb tots els números de l’1 al 1000 que tinguin un 3.

# 8.Comptar el nombre d'espais d'una cadena
#unString = 'Un string qualsevol que té molts espais'

# 9.Treure totes les vocals d'una cadena.

# 10.Cercar totes les paraules d’una cadena de menys de 4 lletres.

# -----------------------------------------------------------------------

#declaració
llistaExemple=[1,2,3,4,5,6]
llistaExemple2=[1,2,3,7,9,10]
unString = 'Un string qualsevol que té molts espais'
vocals ="aeiou"
nova = []
ll = []

exercicis =["Sortir",\
            "Crear llista idèntica a llistaExemple",\
            "Crear llista [1200-1980] pas 130",\
            "Crear llista a partir de l'anterior, +6 als elements",\
            "Crear llista amb els quadrats de llistaExemple",\
            "Crear llista amb els quadrats > 50 de llistaExemple2",\
            "Crear llista [1-1000] divisibles per 7",\
            "Crear llista [1-1000] amb elements que tenen un 3",\
            "Comptar els espais de unString",\
            "Treure totes les vocals de unString",\
            "Cercar paraules < 4 lletres de unString"]
opcio = 1

#menú opcions amb 0 per sortir
while (opcio != 0):

    print("\nList Comprehension")
    
    #mostro a usuari opcions i (posició + 1)
    for i in range(len(exercicis)):
        print("[Opció " + str(i) + "]", exercicis[i])
    #demano opció
    opcio = int( input("\nQuin exercici vols veure ? [1-10] : "))

    print("\nExercici",opcio)
    if opcio == 1:
        ll = [num for num in llistaExemple]
        print(llistaExemple)
        print(ll)
            
    elif opcio == 2:
        ll = [num for num in range(1200,1980+(1),130)]
        print(ll)
        
    elif opcio == 3:
        ll = [num + 6 for num in range(1200,1980+(1),130)]
        print(ll)
    
    elif opcio == 4:
        ll = [num**2 for num in llistaExemple]
        print(llistaExemple)
        print(ll)
    
    elif opcio == 5:
        ll = [num**2 for num in llistaExemple2 if (num**2 > 50)]
        print(llistaExemple2)
        print(ll)
    
    elif opcio == 6:
        ll = [num for num in range(1,1000+(1)) if (num % 7 == 0)]
        print(ll)
    
    elif opcio == 7:
        ll = [num for num in range(1,1000+(1)) if ('3' in str(num))]
        print(ll)
    
    elif opcio == 8:
        ll = [lletra for lletra in unString if (lletra == " ")]
        print(unString)
        print(ll)
        print(len(ll),"espais")
    
    elif opcio == 9:
        ll = [lletra for lletra in unString if (lletra.lower() not in vocals)]
        print(unString)
        for lletra in ll:
            print(lletra, end = "")
        print()
    
    elif opcio == 10:
        ll = [paraula for paraula in unString.split() if len(paraula) < 4]
        print(unString)
        print(ll)
    
    else:
        print("Opció incorrecte")

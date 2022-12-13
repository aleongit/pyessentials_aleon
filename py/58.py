#Aleix Leon

#Programa l’algorisme del sedàs d’Eratòstanes.
#Busca els nombres primers del 2 al 120.
#Busca els 50 primers nombres primers.
# -----------------------------------------------------------------------

#declaració
Min = 2
Max = 120
Q = 50
marca = "."

versions = ["Primers del 2 al 120","Els 50 primers primers"]
opcions = ""

#llista de valors buides
valors =[]
primers = []

print("Algorismes Clàssics: Sedàs d’Eratòstenes")

#preguntem a usuari opció
opcio = 0
while (opcio < 1) or (opcio > len(versions)):
    #mostro a usuari opcions i (posició + 1)
    for i in range(len(versions)):
        print("[Opció " + str(i + 1) + "]", versions[i])
        opcions += "[" + str(i + 1) + "]"
    #demano opció
    opcio = int( input("\nQuina versió triem " + opcions + " ? "))
    opcions = ""

#v = opcions[opcio-1]
if opcio == 1:
    Max = 120
elif opcio == 2:
    Max = 300

#generar N valors a llista segons opció
for i in range(Max + 1):
    valors.append(i)
#print(valors)

#càlculs per comprovar
#import math
#print(math.sqrt(Max))
#print(int((Max)**(1/2)))

#algorisme
for i in range(Min, int((Max)**(1/2)) + 1):
    #print(i)
    if valors[i] != marca:
        for j in range(i, ((Max) // i) + 1):
            #print("la i",i,"-la j",j)
            #print(i*j)
            valors[i*j] = marca

print("\nXIVATO MARCATS", valors)

conta = 0
#poso els primers en llista nova
for v in valors:
    #filtro els no marcats i 0,1 i màxim fins a 50 valors
    if v != marca and v > 1 and conta<Q:
        primers.append(v)
        conta += 1
print()
print(conta, "primers primers")
print(primers)

    

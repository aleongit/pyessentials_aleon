#Aleix Leon
#Repàs

#Entra un any per teclat entre el 1900 i el 1999
#No avancis fins que l’any entrat està dins de l’interval
#Calcula la suma de les xifres de l’any
#Resta de l’any la suma de les xifres
#Comprova que el resultat és divisible per 9

MIN = 1900
MAX = 1999

a = 0
while a < MIN or a > MAX:
    a = int(input("Entra un any entre 1900 i 1999: "))

xifres = list(str(a))
#print(xifres)

xif =""
for el in xifres:
    xif += el + " + "
    
print(xif)

suma = sum([int(i) for i in str(a)])
print(f"la suma de les xifres ", *xifres,f" dóna = {suma}", sep=" + ")
print(f"la suma de les xifres ", xif ,f" dóna = {suma}")
print(f"la suma de les xifres ", " + ".join(xifres) ,f" dóna = {suma}")
#print(*xifres)

print("la resta dóna:", a-suma)

if (a-suma) % 9 == 0:
    print(a-suma, "és divisible per 9")
else:
    print(a-suma, "NO és divisible per 9")

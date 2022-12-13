#Aleix Leon

# Agafa un programa d’ordenació dels que has fet (1 a 3), 
# ordena L1 i 
# fes-lo servir com a entrada del programa de cerca binària.
# -----------------------------------------------------------------------

#declaració
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
nova = []
ll = []

versions =["Inserció","Nan","Bombolla"]
opcions = ""
valor = 1

print("Algorismes Clàssics: Ordenació i Cerca")

#AMPLIACIÓ: vull demanar si utilitzem L1 o llista nova de valors
opcio = 0
while opcio !=1 and opcio != 2: #while per assegurar les opcions
    opcio = int( input("Quina llista ordenem L[1] o NOVA[2]: "))
    
    if opcio == 1:
        ll = L1.copy()
    
    #si es demana NOVA, cal crear-la
    if opcio == 2:
        print("\nVes introduint valors, per acabar 0 o negatiu]")
        #demano valors mentre siguin més grans que 0
        while valor > 0:
            valor = int( input("Valor llista: "))
            #control pel número de tall de bucle, no s'ha de posar a llista
            if valor > 0:
                nova.append(valor)
        ll = nova.copy()

print("\nLlista a ordenar", ll)
print()

#demanem mètode ordenació
opcio = 0
while (opcio < 1) or (opcio > len(versions)):
    #mostro a usuari opcions i (posició + 1)
    #si hi hagués més opcions tindria més sentit
    for i in range(len(versions)):
        print("[Opció " + str(i + 1) + "]", versions[i])
        opcions += "[" + str(i + 1) + "]"
        opcions = ""
    #demano opció
    opcio = int( input("\nCom ordenem " + opcions + " ? "))

v = versions[opcio-1]
#copio valor triat

print("Ordenació", v)

#ordenació segons opció
if opcio == 1:
    #ordenem per inserció
    i = 1
    while i < len(ll):
        x = ll[i] # copiem valor a 'x', que és el valor a insertar
        j = i - 1
        
        while (j >=0) and ll[j] > x: #anirem movent valors cap amunt (fent lloc)
            ll[j+1] = ll[j] # fem lloc per la 'x', pujant el valor cap a la dreta
            j = j - 1
        
        ll[j+1] = x # aquí insertem la 'x'
        i = i + 1

elif opcio == 2:
    #ordenem per nan
    pos = 0
    while pos < len(ll): #fins que no arribem al final de llista
        #si està al principi o la posició és més gran que l'anterior, continua amb la llista
        if (pos == 0) or ll[pos] >= ll[pos-1]:
            pos += 1 #incrementem posició
        #si la posició anterior és mes gran que la actual, tire enrrere la posició actual
        else:
            #intercanviem posició amb posició anterior
            guarda = ll[pos]
            ll[pos] = ll[pos-1]
            ll[pos-1] = guarda
            #decrementem posició, tornem enrere
            pos -= 1

elif opcio == 3:
    #ordenem de la bombolla
    n = len(ll) #agafem mida
    intercanvi = True #boleana per saber si o no intercanvi

    while intercanvi: #mentre hi hagi 'intercanvi'
        intercanvi = False #inicialitzem
        
        for i in range(1, n): #valors de 1 a mida
            #print(i)
            if ll[i-1] > ll[i]:
                #intercanvi de pos actual amb anterior
                aux = ll[i]
                ll[i] = ll[i-1]
                ll[i-1] = aux
                
                intercanvi = True
        n -= 1 #reduim 1 posició cada vegada perquè els valors que deixem a la dreta són els més grans
print() 
print(ll)

#preguntar element a cercar
el = int( input("Valor a cercar ? "))

#apliquem algorisme cerca binària
#inicialitzem variables
trobat = False
inf = 0             #límit inferior la 1a posició
sup = len(ll) - 1   #límit superior serà la longitud de la llista (-1 posició) sinó peta

#fer mentre límit inferior s'apropi o sigui igual a inferior, i no es trobi valor
while (inf <= sup) and (not trobat):
    #busca posició mig, que serà la meitat dels dos límits + la posició inferior anterior
    mig = (sup - inf) // 2 + inf
    #si l'element és igual al valor acotat del mig ,trobat
    if el == ll[mig]:
       trobat = True
    else:
       if el < ll[mig]:
         sup = mig - 1 #decrementem nivell superior
       else:
         inf = mig + 1 #incrementem nivell inferior

print()
if not trobat:
    print(el , "No trobat")
else:
    print(el , "Trobat a la posició", mig)

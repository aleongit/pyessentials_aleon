#Aleix Leon

#taules de multiplicar de 1 al 10 amb FOR's aniuats

T = 10 #constant TAULA
M = 10 #constant MULTIPLICADOR

print("Anem a repassar les taules de multiplicar")

#bucle per les taules amb range 1 a 11[10+1]
for i in range(1, T+1):
    print("Taula del ", i)
    
    #bucle pel multiplicador de la taula amb range 1 a 11[10+1]
    for j in range(1, M+1):
        #print(j)
        print(i, " * ", j , " = ", i * j)
        
    input("Prem tecla per continuar...")
        

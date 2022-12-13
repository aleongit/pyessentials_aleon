#Aleix Leon

#calcular les n primeres potències d’un nombre fent servir el bucle for.
#Per exemple si introduïm el 2 i 4 , la consola mostrarà:
"""
2 elevat a 0 és 1
2 elevat a 1 és 2
2 elevat a 2 és 4
2 elevat a 3 és 8
2 elevat a 4 és 16"""

print("Calculem potències amb Python")

base = int( input("Introdueix la base: "))
potencia = int( input("Introdueix la potència: "))

#bucle de (i = 0) a (potència + 1)
for i in range(potencia + 1):
    print(base, "elevat a", i , "és", base ** i)



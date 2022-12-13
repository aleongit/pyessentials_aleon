#Aleix Leon
#Diccionaris

#Demana un nombre per teclat, comprova que sigui més gran que 1000, i no avancis fins que així sigui
#i després  crea un diccionari on  les claus siguin des del número 1 fins al número indicat, múltiple de 10,
#i els valors siguin la meitat de les claus.
#Fes dues versions, amb bucle for i amb dictionary comprehension 

#declaració
MIN = 1000

#demanem número >1000
n = 0
while n <= MIN:
    n = int( input("Introdueix nombre >1000: "))

#print("avança")
print("Versió amb bucle 'for'")

#defineixo diccionari buit
dic = {}

#bucle for amb condició, només afageixo a dic si és múltiple de 10
for el in range(n+1):
    if el % 10 == 0:
        dic[el] = el//2
        #print(el, dic[el])
print(dic)
    
print("Versió amb dictionary comprehension")

#netejo
dic.clear()

dic = {el : el//2 for el in range(n+1) if el % 10 == 0}
print(dic)


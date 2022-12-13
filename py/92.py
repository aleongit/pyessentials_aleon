#Aleix Leon
#Diccionaris

#Demana una cadena per teclat  i genera un diccionari amb la quantitat aparicions de cada caràcter en la cadena.

#demanem cadena
cadena = input("Introdueix cadena: ")

print("Versió amb dictionary comprehension")

#per cada lletra de cadena, posa clau lletra i conta quantes
dic = {el : cadena.count(el) for el in cadena}
print(dic)


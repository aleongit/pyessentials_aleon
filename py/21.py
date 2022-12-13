#Aleix Leon
#demanar num fins número negatiu amb while
#dir si num parell/senar amb while

#inicialitzo num a 0 per entrar al 'while'
num = 0

#fem bucle mentre num >= 0
#si s'entra número negatiu, surt del bucle
while num >= 0:

  #demanem num enter
  num = int(input ("Entra un número enter: "))

  #càlculs per si 'parell' o 'senar'
  if num % 2 == 0:
    print("El número", num, "és parell")
  
  else:
    print("El número", num, "és senar")
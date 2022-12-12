#parell / senar

#assignació variable directe a l'entrada

#FORÇO A ENTER
#converteixo l'string de l'input a INT, passant primer a Float per si hi ha decimals, sinó peta
#amb lletres peta, pendent controlar

num = int(float(input ("Introdueix un número enter: ")))
#num = int(float(num))
#print (num)

if num % 2 == 0:
    print("El número", num, "és parell")
else:
    print("El número", num, "és senar")



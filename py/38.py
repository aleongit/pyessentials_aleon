#Aleix Leon

#eliminar element n-èssim de la llista introduïda per teclat.
#Llista de mostres: ['Vermell', 'Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']
#Element = 0
#Sortida ['Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']

#definim llista buida
ll = []

#demanem mida
mida = int (input("Quina mida vols per la llista: "))

#bucle per recorre llista per index (de 0 a mida)
for i in range(mida):
    #demano string per cada posició
    valor = input("Introdueix valor per posició " + str(i) + " de la llista: ")
    #afageixo al final de la llista
    ll.append(valor)

#demanar element a eliminar
print("Llista introduïda:", ll)

#bucle while per demanar valors de posicions permesos
#de 0 a mida -1
#inicialitzo 'po' per entrar
po = -1
while not ((po >= 0) and (po < mida)):
  po = int(input ("Posició d'element a eliminar? "))

#borro element a la posició
ll.remove(ll[po])

print("Llista actualitzada:", ll)

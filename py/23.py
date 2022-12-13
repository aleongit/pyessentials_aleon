#Aleix Leon

#Contrasenya
    #Comenci per la lletra A
    #Tingui una llargada mínima de 6 caràcters
    #Tingui una llarga màxima de 16 caràcters
    #Contingui 1 dels següents caràcters especials ( ) / ! $ % & 
#Demanar contrasenyes fins que sigui ok (amb while)

#constants
MIN = 6
MAX = 16
#string especials
e = "()/!$%&"


#boleana per si contrasenya ok
ok = False

while not ok:
    #demanem contrasenya
    contrasenya = input ("Entra contrasenya: ")
    
    if contrasenya[0] == 'A':
        
        #print ("OK A")
        mida = len(contrasenya)
        #print (mida)
        
        if mida < MIN :
          print("La contrasenya ha de tenir mínim 6 caràcters")
        elif mida > MAX:
          print("La contrasenya ha de tenir màxim 16 caràcters")
        else:
          #print ("OK MIDA")
          #ok = True
          if e[0] in contrasenya or e[1] in contrasenya or e[2] in contrasenya \
          or e[3] in contrasenya or e[4] in contrasenya or e[5] in contrasenya \
          or e[6] in contrasenya:
              print("Contrasenya OK")
              ok = True
          else:
              print("La contrasenya ha de tenir algun caràcter especial ( ) / ! $ % &")            
    else:
        print("La contrasenya no comença per A")


   
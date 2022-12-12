#entrar només una lletra i dir si és vocal o consonant

#importo string amb totes les lletres, així controlo només lletres.
#i així descarto números i altres caràcters
import string
totes = string.ascii_letters
print("Lletres disponibles:",totes)

#defineixo vocals en mínuscules
vocals = "aeiou"

#demanar lletra
lletra = input ("Introdueix una lletra: ")

llargada = len(lletra)
#print (llargada)

#comprovo només 1 lletra, sinó agafo la 1a posició
if llargada != 1:
    print (lletra, "Has entrat més d'una lletra \nAgafo la 1a")
    lletra = lletra[0]
    #print (lletra)

#converteixo lletra a minúscules
lletra = lletra.lower()

#miro si la lletra està en la cadena vocals, sinó miro a llista completa, i sinó NO és una lletra
if lletra in vocals:
    print(lletra," és una VOCAL")
elif lletra in totes:
    print(lletra," és una CONSONANT")
else:
    print(lletra," NO és una LLETRA")
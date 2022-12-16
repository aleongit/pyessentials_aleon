import sys

import unicodedata

import string
#print(string.ascii_letters) # lletres ascii
#print(string.digits)        # digits
#print(string.punctuation)   # símbols puntuació
#print(string.printable)     # caràcters printables

import datetime
#x = datetime.datetime.now()
#print(x.year)
#print(x.strftime("%A"))
#x = datetime.datetime(2020, 5, 17)
#print(x.strftime("%A"))

vocals ="aeiou"

#funció trobada per control accents
def treu_accents(ca):
    """
    Removes unicode accents from a string, downgrading to the base character
    """
    nfkd = unicodedata.normalize('NFKD', ca)
    return u"".join([c for c in nfkd if not unicodedata.combining(c)]) 

def nomes_lletres(ca):
    return len(ca) == len([c for c in ca if c in string.ascii_letters])

def nomes_digits(ca):
    return len(ca) == len([c for c in ca if c in string.digits])

def vocal(c):
    return c in vocals

#conta per cada vocal
def conta_vocal(ca):
    #vocal + contador de la vocal per cada lletra de frase si és vocal
    #dicionari
    return {c: ca.count(c) for c in ca if vocal(c)}

#conta vocals
def conta_vocals(ca):
    return len([c for c in ca if vocal(c)])

def arg():
    # nombre d'arguments
    return len(sys.argv)-1

# si troba algun element 'no només lletres' afageix
# si tots són 'només lletres' serà 0
def tots_lletres(ll):
    ll = [el for el in ll if not nomes_lletres(treu_accents(el))]
    return ll

def dia_dma(ca):
    #dd/mm/aaaa
    try:
       r = datetime.datetime.strptime(ca,'%d/%m/%Y')
       return r.strftime("%A")
    except ValueError:
       print("Format de data incorrecte. Ha de ser [dd/mm/aaaa] vàlid")
       return None

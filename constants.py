# -*- coding: utf-8 -*-
# Aleix Leon

# constants ______________________________________________
AUTOR = "aleon"

ESSENTIALS = {
    '11': {
        'script': 'py/11.py',
        'category': 'Condicionals - If',
        'title': 'Parell o imparell',
        'text': """Fes un programa que donat un número sencer que introduïm per teclat ens digui si és parell o és imparell:
Per l’entrada 5 mostrarà per consola:
El número 5 és imparell
        """,
    },
    '12':  {
        'script': 'py/12.py',
        'category': 'Condicionals - If',
        'title': 'Múltiple de 5 o de 7',
        'text': """Escriviu un programa Python per comprovar que un nombre que introduïm per teclat és múltiple de  7 i múltiple de 5
        """,
    },
    '13':  {
        'script': 'py/13.py',
        'category': 'Condicionals - If',
        'title': 'Endevinar nombre',
        'text': """Fes un programa per endevinar un nombre entre l’1 i el 9 (ambdós inclosos) que es genera aleatòriament.
L’usuari introduirà el nombre per teclat i el programa retornarà:
si l’ha encertat : ENHORABONA!! Ets un crack!
si no. Si la diferència és només d’1:
casi, pels pèls!
si la diferència  és més  4: dedica’t al parxís
si no: la propera vegada ho faràs millor
        """,
    },
    '14':  {
        'script': 'py/14.py',
        'category': 'Condicionals - If',
        'title': 'Vocal o consonant',
        'text': """Entrar només una lletra i dir si és vocal o consonant
        """,
    },
    '15':  {
        'script': 'py/15.py',
        'category': 'Condicionals - If',
        'title': 'Comprobació cadena',
        'text': """Escriu un programa que donat un string que cal introduir per teclat, comprovi si:
És de mida superior a 10 caràcters
És de mida inferior a 10 caràcters i conté algun dels següents caràcters: * + / -
És de mida 10 caràcters i comença per -
És de mida 10 caràcters i acaba per .
        """,
    },
    '21':  {
        'script': 'py/21.py',
        'category': 'Loops - while',
        'title': 'Demanar número fins número negatiu',
        'text': """Fes un programa que vagi demanant números per teclat
fins que introduïm un número negatiu i mostri per pantalla,
per cada número entrat, si és parell o és senar.
        """,
    },
    '22':  {
        'script': 'py/22.py',
        'category': 'Loops - while',
        'title': "Demanar número fins endevinar-l'ho",
        'text': """Modifica l’algorisme d’endevinar un nombre. El programa demanarà
nombres fins que l’encertis..
        """,
    },
    '23':  {
        'script': 'py/23.py',
        'category': 'Loops - while',
        'title': "Demanar contrasenya fins que sigui vàlida",
        'text': """Fes un algorisme que comprovi la validesa d’un password.
Demanarem el password per teclat i hem de comprovar que:
Comenci per la lletra ‘A’
Tingui una llargada mínima de 6 caràcters
Tingui una llarga màxima de 16 caràcters
Contingui 1 dels següents caràcters especials ( ) / ! $ % & 
L’usuari haurà de continuar introduint strings fins que n’introdueixi un de vàlid.
        """,
    },
    '31':  {
        'script': 'py/31.py',
        'category': 'Loops - for',
        'title': "Sumar tots els números d'una llista",
        'text': """Fes un programa que suma un valor introduït per teclat a tots els elements
de la llista [1,2,3,4,5,6,7,8,9,10] utilitzant un bucle for, cal modificar
la llista original.
        """,
    },
    '32':  {
        'script': 'py/32.py',
        'category': 'Loops - for',
        'title': "Taules de multiplicar",
        'text': """Fes un programa en python que imprimeix les taules de multiplicar
de l’1 a 10 amb un for niuat.
        """,
    },
    '33':  {
        'script': 'py/33.py',
        'category': 'Loops - for',
        'title': "Potències",
        'text': """Fes un programa que calculi les n primeres potències d’un nombre fent servir
el bucle for.
        """,
    },
    '34':  {
        'script': 'py/34.py',
        'category': 'Loops - for',
        'title': "Multiplicar números d'una llista",
        'text': """Escriviu un programa que mostri per pantalla el resultat de sumar i el
resultat de multiplicar tots els elements d'una llista. Cal introduir la llista per
teclat. Ajuda: feu servir un bucle per afegir elements a la llista.
        """,
    },
    '35':  {
        'script': 'py/35.py',
        'category': 'Loops - for',
        'title': "Número més gran, més petit i mitjana de números d'una llista",
        'text': """Escriviu un programa per obtenir el nombre més gran, més petit i la mitjana d'una llista
de sencers. Cal introduir la llista per teclat. Fer versió bucle i versió mètodes.
        """,
    },
    '36':  {
        'script': 'py/36.py',
        'category': 'Loops - for',
        'title': "Trobar elements d'una llista per condició",
        'text': """Escriviu un programa que donada una llista de strings, no cal que sigui introduïda
per teclat, ens digui quants elements hi ha a la llista de longitud més gran o igual
que 2, i comencen per ‘a’. Mostrar per pantalla el resultat.
Ex: ['abc', 'xyz', 'aba', '1221', ‘a’] -> sortida 2 elements
        """,
    },
    '37':  {
        'script': 'py/37.py',
        'category': 'Loops - for',
        'title': "Eliminar duplicats d'una llista",
        'text': """Escriviu un programa per eliminar duplicats d'una llista.
Bucle i funció integrada de pyhton.
        """,
    },
    '38':  {
        'script': 'py/38.py',
        'category': 'Loops - for',
        'title': "Eliminar elements d'una llista per posició",
        'text': """Escriviu un programa que elimina l’element n-èssim de la llista
introduïda per teclat.
        """,
    },
    '39':  {
        'script': 'py/39.py',
        'category': 'Loops - for',
        'title': "Eliminar elements d'una llista per condició",
        'text': """Escriviu un programa per imprimir els números d'una llista
especificada per teclat i després d'eliminar-ne els números parells.
        """,
    },
    '310':  {
        'script': 'py/310.py',
        'category': 'Loops - for',
        'title': "Elements en comú de dues llistes",
        'text': """Escriviu un programa que comprova si dues llistes tenen elements
en comú. P.exemple: llista1 = [1,2,3,4,5,6,7], llista2 = [4,1,20,100]
imprimeix per pantalla “Tenen 2 elements en comú i són: 1,4”
        """,
    },
}

# classes objecte ______________________________________________

# funcions ______________________________________________

# -*- coding: utf-8 -*-
# Aleix Leon

# constants ______________________________________________
AUTOR = "aleon"

CATEGORIES = [
    'Conditionals [If]',
    'Loops [while]',
    'Loops [for] and lists',
    'Mastermind',
    'Classics',
    'List Comprehension',
    'Tuples',
    'Set',
    'Dictionaries',
]

ESSENTIALS = {
    '11': {
        'script': 'py/11.py',
        'category': CATEGORIES[0],
        'title': 'Parell o imparell',
        'text': """Fes un programa que donat un número sencer que introduïm per teclat ens digui si és parell o és imparell:
Per l’entrada 5 mostrarà per consola:
El número 5 és imparell
        """,
    },
    '12':  {
        'script': 'py/12.py',
        'category': CATEGORIES[0],
        'title': 'Múltiple de 5 o de 7',
        'text': """Escriviu un programa Python per comprovar que un nombre que introduïm per teclat és múltiple de  7 i múltiple de 5
        """,
    },
    '13':  {
        'script': 'py/13.py',
        'category': CATEGORIES[0],
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
        'category': CATEGORIES[0],
        'title': 'Vocal o consonant',
        'text': """Entrar només una lletra i dir si és vocal o consonant
        """,
    },
    '15':  {
        'script': 'py/15.py',
        'category': CATEGORIES[0],
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
        'category': CATEGORIES[1],
        'title': 'Demanar número fins número negatiu',
        'text': """Fes un programa que vagi demanant números per teclat
fins que introduïm un número negatiu i mostri per pantalla,
per cada número entrat, si és parell o és senar.
        """,
    },
    '22':  {
        'script': 'py/22.py',
        'category': CATEGORIES[1],
        'title': "Demanar número fins endevinar-l'ho",
        'text': """Modifica l’algorisme d’endevinar un nombre. El programa demanarà
nombres fins que l’encertis..
        """,
    },
    '23':  {
        'script': 'py/23.py',
        'category': CATEGORIES[1],
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
        'category': CATEGORIES[2],
        'title': "Sumar tots els números d'una llista",
        'text': """Fes un programa que suma un valor introduït per teclat a tots els elements
de la llista [1,2,3,4,5,6,7,8,9,10] utilitzant un bucle for, cal modificar
la llista original.
        """,
    },
    '32':  {
        'script': 'py/32.py',
        'category': CATEGORIES[2],
        'title': "Taules de multiplicar",
        'text': """Fes un programa en python que imprimeix les taules de multiplicar
de l’1 a 10 amb un for niuat.
        """,
    },
    '33':  {
        'script': 'py/33.py',
        'category': CATEGORIES[2],
        'title': "Potències",
        'text': """Fes un programa que calculi les n primeres potències d’un nombre fent servir
el bucle for.
        """,
    },
    '34':  {
        'script': 'py/34.py',
        'category': CATEGORIES[2],
        'title': "Multiplicar números d'una llista",
        'text': """Escriviu un programa que mostri per pantalla el resultat de sumar i el
resultat de multiplicar tots els elements d'una llista. Cal introduir la llista per
teclat. Ajuda: feu servir un bucle per afegir elements a la llista.
        """,
    },
    '35':  {
        'script': 'py/35.py',
        'category': CATEGORIES[2],
        'title': "Número més gran, més petit i mitjana de números d'una llista",
        'text': """Escriviu un programa per obtenir el nombre més gran, més petit i la mitjana d'una llista
de sencers. Cal introduir la llista per teclat. Fer versió bucle i versió mètodes.
        """,
    },
    '36':  {
        'script': 'py/36.py',
        'category': CATEGORIES[2],
        'title': "Trobar elements d'una llista per condició",
        'text': """Escriviu un programa que donada una llista de strings, no cal que sigui introduïda
per teclat, ens digui quants elements hi ha a la llista de longitud més gran o igual
que 2, i comencen per ‘a’. Mostrar per pantalla el resultat.
Ex: ['abc', 'xyz', 'aba', '1221', ‘a’] -> sortida 2 elements
        """,
    },
    '37':  {
        'script': 'py/37.py',
        'category': CATEGORIES[2],
        'title': "Eliminar duplicats d'una llista",
        'text': """Escriviu un programa per eliminar duplicats d'una llista.
Bucle i funció integrada de pyhton.
        """,
    },
    '38':  {
        'script': 'py/38.py',
        'category': CATEGORIES[2],
        'title': "Eliminar elements d'una llista per posició",
        'text': """Escriviu un programa que elimina l’element n-èssim de la llista
introduïda per teclat.
        """,
    },
    '39':  {
        'script': 'py/39.py',
        'category': CATEGORIES[2],
        'title': "Eliminar elements d'una llista per condició",
        'text': """Escriviu un programa per imprimir els números d'una llista
especificada per teclat i després d'eliminar-ne els números parells.
        """,
    },
    '310':  {
        'script': 'py/310.py',
        'category': CATEGORIES[2],
        'title': "Elements en comú de dues llistes",
        'text': """Escriviu un programa que comprova si dues llistes tenen elements
en comú. P.exemple: llista1 = [1,2,3,4,5,6,7], llista2 = [4,1,20,100]
imprimeix per pantalla “Tenen 2 elements en comú i són: 1,4”
        """,
    },
    '41':  {
        'script': 'py/41.py',
        'category': CATEGORIES[3],
        'title': "Joc Mastermind amb ús de bucles, condicionals i llistes.",
        'text': """Es generarà una seqüència aleatòria de mida 4 que serà una combinació de “ABCDE”,
pot haver-hi lletres repetides, per exemple AABB, ACBD, ADAB, BBDC, etc.
FOR concatenant random choise x lletra, tantes vegades com lletra
l'usuari té 5 vides, és a dir 5 possibilitats per intentar encertar la combinació.

Mentre no hagi encertat la combinació, i encara tingui vides fer:
Resta una vida.
Mostra els intents que ha fet fins el moment.
Demana combinació per teclat i no avança fins que no sigui combinació possible
(mida 4 i formada per les lletres possibles)
Compta quantes lletres encertades estan en la posició correcta.
Marca aquestes posicions per evitar comptar-les dues vegades.
Compta quantes lletres encertades en posició incorrecta hi ha.
Marca aquestes posicions per evitar comptar-les dues vegades.

Si la combinació és guanyadora,
Mostra missatge d’enhorabona i finalitza el programa.

En altre cas:
Mostra quines lletres en posició correcta hi ha amb el símbol #
Mostra quines lletres encertades hi ha en posició incorrecta amb el símbol *
Mostra les lletres no existents a la combinació amb el símbol -
Per exemple si la combinació guanyadora és AACB i l’usuari entra ACDE ha de mostrar # * - -. La A és correcta i està en la posició correcta #, la C és correcta en posició incorrecta * i la resta D E no encertades, per tant - -.
   A B C D
   A A B B
   # - * * (La que encertem ja la marquem com encertada)
""",
    },
    '51':  {
        'script': 'py/51.py',
        'category': CATEGORIES[4],
        'title': "Algorisme ordenació per inserció",
        'text': """Programa l’algorisme d’ordenació per inserció. Prova’l amb L1 i L2.
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
        """,
    },
    '52':  {
        'script': 'py/52.py',
        'category': CATEGORIES[4],
        'title': "Algorisme ordenació del nan",
        'text': """Programa l’algorisme d’ordenació del nan. Prova’l amb L1 i L2.
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
        """,
    },
    '53':  {
        'script': 'py/53.py',
        'category': CATEGORIES[4],
        'title': "Algorisme ordenació de la bombolla",
        'text': """Programa l’algorisme d’ordenació de la bombolla. Prova’l amb L1 i L2.
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
        """,
    },
    '54':  {
        'script': 'py/54.py',
        'category': CATEGORIES[4],
        'title': "Algorisme de cerca seqüencial",
        'text': """Programa l’algorisme de cerca seqüencial. Prova’l amb L1 i L2.
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
        """,
    },
    '55':  {
        'script': 'py/55.py',
        'category': CATEGORIES[4],
        'title': "Algorisme de cerca seqüencial amb llista ordenada",
        'text': """Programa l’algorisme de cerca seqüencial amb llista ordenada. Prova’l amb L3.
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]
        """,
    },
    '56':  {
        'script': 'py/56.py',
        'category': CATEGORIES[4],
        'title': "Algorisme de cerca binària",
        'text': """Programa l’algorisme de cerca binària. Prova’l amb L3 i un valor entrat per teclat
        """,
    },
    '57':  {
        'script': 'py/57.py',
        'category': CATEGORIES[4],
        'title': "Algorisme d'Euclides",
        'text': """Programa l’algorisme d'Euclides (les dues versions). Prova’l amb 1071 i 462.
Per MCD (=màxim comú divisor)
        """,
    },
    '58':  {
        'script': 'py/58.py',
        'category': CATEGORIES[4],
        'title': "Algorisme del sedàs d'Eratòstanes",
        'text': """Programa l’algorisme del sedàs d’Eratòstanes.
Busca els nombres primers del 2 al 120.
Busca els 50 primers nombres primers.
        """,
    },
    '59':  {
        'script': 'py/59.py',
        'category': CATEGORIES[4],
        'title': "Algorisme del xifratge del Cèsar",
        'text': """Programa l’algorisme del xifratge del Cèsar.
Fes dues versions en Python: amb llistes i amb cadenes.
Prova'l amb la frase "m'agraden els algorismes classics".
        """,
    },
    '510':  {
        'script': 'py/510.py',
        'category': CATEGORIES[4],
        'title': "Combinació d'algorismes clàssics",
        'text': """# Agafa un programa d’ordenació dels que has fet (1 a 3), 
# ordena L1 i fes-lo servir com a entrada del programa de cerca binària.
        """,
    },
    '61':  {
        'script': 'py/61.py',
        'category': CATEGORIES[5],
        'title': "List Comprehension - 10 exercicis amb menú",
        'text': """1.Crear una llista idèntica a llistaExemple mitjançant la comprensió de la llista.
llistaExemple=[1,2,3,4,5,6]

2.Crear una llista a partir dels elements d'un interval de 1200 a 1980 ambdós inclosos,
amb passos de 130, mitjançant la comprensió de la llista.

3.Crear una llista nova a partir de l’anterior, però sumeu 6 a cada element.

4.Crear una llista que sigui els quadrats de cada element de la llista.
llistaExemple=[1,2,3,4,5,6]

5.Crear una llista a partir dels quadrats de cada element de la llista si el quadrat > 50.
llistaExemple2=[1,2,3,7,9,10]

6.Crear una llista amb tots els números de l’1 al 1000 que són divisibles per 7.

7.Crear una llista amb tots els números de l’1 al 1000 que tinguin un 3.

8.Comptar el nombre d'espais d'una cadena
unString = 'Un string qualsevol que té molts espais'

9.Treure totes les vocals d'una cadena.

10.Cercar totes les paraules d’una cadena de menys de 4 lletres.
""",
    },
    '71':  {
        'script': 'py/71.py',
        'category': CATEGORIES[6],
        'title': "Tuples - 11 exercicis amb menú",
        'text': """1. Crear una tupla nova que sigui la tupla girada (al revés)
aTuple = (10, 20, 30, 40, 50)

2. Crar una tupla d’un sol element anomenada unSol i amb contingut 50

3. Fer un swap de les següents tuples 2 versions, amb variable auxiliar i directament
tuple1 = (99, 88)
tuple2 = (11, 22)

4. Ordena la tupla pel segon element: algorismes treballats (bombolla, nan o inserció)
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
sortida esperada (('c', 11), ('a', 23), ('d', 29), ('b', 37))

5. Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?
tuple1 = (50, 10, 60, 70, 50)

6. Comprova si tots els ítems de la tupla tenen el mateix valor
tuple1 = (45, 45, 45, 45)

7. Com es crea una tupla buida? Com es converteix una tupla en una llista?

8. Tenint una llista de números, crear una llista de tuples amb el 1r element com a número i el 2n com a cub del número.
Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

9. Fes una llista de tuples de totes les combinacions possibles de 2 tuples d'arguments. 
Input : t1 = (7, 2), t2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

10. Trobar els elements repetits d’una llista i construir una llista de tuples
on surti en primer terme l’element i en segon terme quantes vegades apareix.
llista = [1,2,3,1,2,1,1]
sortida = [(1,4),(2,2),(3,1)]

11. Troba en quina posició es troba l’element 20:
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
        """,
    },
    '81':  {
        'script': 'py/81.py',
        'category': CATEGORIES[7],
        'title': "Set - 7 exercicis amb menú",
        'text': """
        """,
    },
    '91':  {
        'script': 'py/91.py',
        'category': CATEGORIES[8],
        'title': "Crear diccionaris amb bucle i dictionary comprehension",
        'text': """Demana un nombre per teclat, comprova que sigui més gran que 1000, i no avancis fins que així sigui
i després  crea un diccionari on les claus siguin des del número 1 fins al número indicat, múltiple de 10,
i els valors siguin la meitat de les claus.
Fes dues versions, amb bucle for i amb dictionary comprehension 
        """,
    },
    '92':  {
        'script': 'py/92.py',
        'category': CATEGORIES[8],
        'title': "Crear diccionari a partir de cadena",
        'text': """Demana una cadena per teclat  i genera un diccionari amb la quantitat aparicions de cada caràcter en la cadena
        """,
    },
    '93':  {
        'script': 'py/93.py',
        'category': CATEGORIES[8],
        'title': "Bàscula de fruiteria",
        'text': """Programar una bàscula d’una fruiteria. L’objectiu serà fer el tiquet de cada venda. Declara un diccionari.
El diccionari tindrà com a clau el nom de les fruites, i com a valor el preu per kg de la fruita indicada
(fes un diccionari que tingui 5 tipus de fruites diferents).
Un cop creat el diccionari demana per cada fruita el pes, i acumula en una variable import.
Has d’imprimir en un format net i polit un tiquet similar a l’exemple.
        """,
    },
    '94':  {
        'script': 'py/94.py',
        'category': CATEGORIES[8],
        'title': "Notes alumnes",
        'text': """Funcionalitats: Afegir Alumne, Eliminar alumne, Afegir  notes a alumne (mòdul, nota),
llistat de tots els alumnes (la llista de tots els alumnes),
llistat d’un alumne (el nom de l’alumne i totes les seves notes),
estadístiques (que responen a les qüestions més avall) i sortir.

Demana els noms dels alumnes per teclat, els noms dels alumnes d'una classe i les notes que han obtingut.
Cada alumne pot tenir diferent quantitat de notes, que també  s’introduiran per teclat, 
valida que siguin notes entre 0 i 10.
Guarda la informació en un diccionari, les claus seran els noms dels alumnes i els valors seran llistes de tuples
de parelles de tuples  (modul, nota) per emmagatzemar les notes de cada alumne.
        """,
    },
}

# classes objecte ______________________________________________

# funcions ______________________________________________

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
    'Review',
    'Functions',
    'Functions with return',
    'Functions & 2D arrays'
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
    '101':  {
        'script': 'py/101.py',
        'category': CATEGORIES[9],
        'title': "Entre 1900 i 1999",
        'text': """Entra un any per teclat entre el 1900 i el 1999
No avancis fins que l’any entrat està dins de l’interval
Calcula la suma de les xifres de l’any
Resta de l’any la suma de les xifres
Comprova que el resultat és divisible per 9
        """,
    },
    '102':  {
        'script': 'py/102.py',
        'category': CATEGORIES[9],
        'title': "Carl Friedrich Gauss tenia raó",
        'text': """Fes un bucle que demani un nombre enter 
Surt del bucle quan l’usuari entri un enter entre 1 i 20 per teclat

Calcula el resultat de la fórmula n·(n+1) / 2. 
Compte: el resultat de la fórmula ha de ser enter

Imprimeix per pantalla el resultat anterior

Fes un bucle que sumi els enters des d’1 fins al nombre entrat per teclat
Compara el resultat de la fórmula amb la suma calculada en el bucle
Si són iguals escriu “Carl Friedrich Gauss tenia raó”
Sinó escriu “Alguna cosa ha fallat”
        """,
    },
    '103':  {
        'script': 'py/103.py',
        'category': CATEGORIES[9],
        'title': "Meteo",
        'text': """Aquí teniu una llista de diccionaris de les dades metereològiques d'alguns observatoris de Catalunya
Les claus de cada diccionari són ['Observatori', 'Alt.', 'Temp. Actual', 'Temp. Màx', 'Temp. Min', 'Humitat Act', 'Humitat Màx', 'Humitat Mín', 'Baròmetre Act', 'Baròmetre Màx', 'Baròmetre Mín', 'Vent Act', 'Vent Màx', 'Precip Avui', 'Precip Any', 'IR']
# Exercici 1:
De quants observatoris tenim dades?
Troba en quina població fa més fred actualment,
en quina han tingut la temperatura màxima més alta,
quina és la mitjana de les temperatures mínimes

# Exercici 2:
Crea una llista de tuples amb el nom de la població i la precipiació acumulada anual
Ordena la llista per precipitació acumulada utilitzant algun dels algorismes d'ordenació treballats a classe 
quines 5 poblacions hi ha plogut més?

# Exercici 3
Fes una llista a partir de dadesMeteo que només hi hagi les poblacions que estan per sobre els 500 metres d'alçada
quantes poblacions hi ha que compleixin aquest criteri?

# Exercici 4
Fes un estudi dels observatoris de la ciutat de Barcelona, 
crea una llista de tuples de 3 elements, el nom de l'Observatori, la humitat actual, i la ratxa màxima de vent dels observatoris de la ciutat de Barcelona
En quin hi fa més vent?
En quin hi ha menys humitat actualment?

# Exercici 5:
Imprimeix les dades en un format net i polit
        """,
    },
    '111':  {
        'script': 'py/111.py',
        'category': CATEGORIES[10],
        'title': "Funcions",
        'text': """Fes un programa en Python amb un menú per fer la crida a cadascuna de les següents funcions., cap de les funcions té retorn.

Nom funció: Multiplica. Funcionalitat: calcula i imprimeix el resultat de multiplicar dos números introduïts per teclat, els inputs es fan a fora de la funció.

Nom funció: anys2000. Funcionalitat: Input a dins de la funció.Demana a l’usuari l’any actual i escriu: “Des del 2000 han passat x anys”, substituint la x pel nombre d’anys que han introduït.

Nom funció tiquetFruita. Funcionalitat: tiquet fruita fet a la tasca de dicionaris 9.

Nom funció:  notaUF. Funcionalitat: Demana la nota de l’examen i la nota de pràctiques. Fa el càlcul següent: 
Només fa mitja si les dues notes són més grans o iguals que 4
Nota Mòdul = 70% * NotaEx +30% * NotaPr
Si la nota és més gran o igual que 5 arrodoneix i imprimeix el literal corresponent ( 5 Aprovat, 6 Bé, 7 8 Notable, 9 10 Excel·lent)
Si està suspès demana si ha comprat un pernil al professor/a. Si és que sí imprimeix “aprovat perniler”.
        """,
    },
    '121':  {
        'script': 'py/121.py',
        'category': CATEGORIES[11],
        'title': "Funcions amb retorn",
        'text': """Modifica l’exercici anterior substituint els prints per returns
        """,
    },
    '122':  {
        'script': 'py/122.py',
        'category': CATEGORIES[11],
        'title': "+ Funcions amb retorn",
        'text': """Fes un altre programa en python amb un menú per fer la crida a les següents funcions:

Nom funció:  factorial. Funcionalitat: Calcula el factorial d'un número (un enter no negatiu). La funció accepta el nombre com a paràmetre i retorna el factorial, o bé un error (-1), el missatge d’error s’imprimirà després de la crida.

Nom funció:  comptaMajusMinus. Funcionalitat: accepta una cadena com a paràmetre  i retorna el nombre de lletres majúscules i minúscules. Cadena de mostra: ‘Una Cadena De Prova' Sortida esperada: (4,12). El missatge es mostra després de la crida. 

Nom funció:  llistaUnitaria. Funcionalitat: Donada una  llista que li passem com paràmetre, retorna una nova llista amb elements únics de la primera llista. Llista de mostres: [1,2,3,3,3,3,4,5] Llista unitària: [1, 2, 3, 4, 5]. No es pot utilitzar la comanda set.

Nom funció:  primer. Funcionalitat: Escriu una funció Python que pren un nombre com a paràmetre menor que 10000 i comproveu si el número és primer o no, o bé error. (podeu utilitzar l’algoritme del sedàs d’Eratòstanes)

Nom funció parells: Funcionalitat: Retorna els números parells d'una llista determinada passada com paràmetre. Llista de mostres: [1, 2, 3, 4, 5, 6, 7, 8, 9] Resultat esperat: [2, 4, 6, 8] 

Nom funció perfecte: Funcionalitat: Escriviu una funció Python per comprovar si un número és perfecte o no. Segons Wikipedia: En la teoria de nombres, un nombre perfecte és un enter positiu que és igual a la suma dels seus divisors positius correctes, és a dir, la suma dels seus divisors positius excloent el nombre en si (també conegut com la seva suma alíquota). De forma equivalent, un nombre perfecte és un nombre que és la meitat de la suma de tots els seus divisors positius (incloent-hi). Exemple: el primer nombre perfecte és 6, perquè 1, 2 i 3 són els seus divisors positius correctes, i 1 + 2 + 3 = 6. Igualment, el número 6 és igual a la meitat de la suma de tots els seus divisors positius: (1 + 2 + 3 + 6) / 2 = 6. El següent número perfecte és 28 = 1 + 2 + 4 + 7 + 14. 

Nom funció palíndrom: Funcionalitat: verifica si una cadena passada com paràmetre és palíndrom o no.
        """,
    },
    '131':  {
        'script': 'py/131.py',
        'category': CATEGORIES[12],
        'title': "Funcions i Matrius de 2 dimensions",
        'text': """Programa la funció matriu2d, que li passes 2 nombres enters n1, n2 i retorna una matriu m de 2 dimensions n1 x n2 plena de nombres aleatoris entre l’1 i el 100.
Programa la funció printMatriu, que imprimeix la matriu que li passes com a paràmetre de manera similar a l’exemple:

Exemple:
m = [[82, 38, 49, 44, 70, 31, 51, 86, 74, 22], [40, 71, 99, 53, 89, 62, 8, 36, 1, 2], [51, 100, 51, 58, 88, 60, 73, 84, 16, 75], [39, 85, 61, 18, 97, 94, 9, 86, 6, 71], [38, 76, 27, 30, 35, 53, 67, 94, 38, 58]]
================= Funció printMatriu ===========================
82 38 49 44 70 31 51 86 74 22
40 71 99 53 89 62  8 36  1  2
51 100 51 58 88 60 73 84 16 75
39 85 61 18 97 94  9 86  6 71
38 76 27 30 35 53 67 94 38 58

Programa la funció llistaMultiples que li passes la matriu m de 2 dimensions com a argument, i un enter e entre l’1 i el 10 i retorna una llista ll d’1 dimensió formada pels múltiples d’e existents a la matriu.
Ex:
llistaMultiples(m,5) per a la mateixa matriu de l’exemple 2 anterior.
genera la sortida: ll = [70, 40, 100, 60, 75, 85, 30, 35]

Programa la funció llistaUnica que li passes la matriu m i retorna una llista única (sense elements repetits) d’1 dimensió.
Exemple: llistaUnica(m)) genera la sortida:
[82, 38, 49, 44, 70, 31, 51, 86, 74, 22, 40, 71, 99, 53, 89, 62, 8, 36, 1, 2, 100, 58, 88, 60, 73, 84, 16, 75, 39, 85, 61, 18, 97, 94, 9, 6, 76, 27, 30, 35, 67]

Programa la funció minMax que retorna el mínim i el màxim de la matriu m que li passes com a paràmetre.
Exemple: minMax(m)  genera la sortida:
(1, 100)

Programa la funció acabaEn que li passes la matriu m com a argument, i un enter e entre l’0 i el 9 i retorna una llista d’1 dimensió formada pels nombres que la seva última xifra és e.
Exemple: acabaEn(m,5) genera la sortida:
[75, 85, 35]

Programa la funció quadrat que donat un sencer s entre 10 i 20 retorna una matriu quadrada de 2 dimensions de mida s x s inicialitzada al caràcter que li passes com a segon paràmetre.
Exemple: quadrat(19,"*") genera la sortida:
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *

Programa la funció inicialitza que inicialitza tots els elements de la matriu al caràcter que li passes per argument. (arguments, la matriu q i el caràcter c).
Exemple: inicialitza(qua,"-") genera la sortida:
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - -

Programa la funció diagonal que posa en les diagonals de la matriu quadrada q, el caràcter c. Es passen com a paràmetres de la funció q i c.

Exemple: diagonal(qua,"*") genera la sortida:
* - - - - - - - - - - - - - - - - - *
- * - - - - - - - - - - - - - - - * -
- - * - - - - - - - - - - - - - * - -
- - - * - - - - - - - - - - - * - - -
- - - - * - - - - - - - - - * - - - -
- - - - - * - - - - - - - * - - - - -
- - - - - - * - - - - - * - - - - - -
- - - - - - - * - - - * - - - - - - -
- - - - - - - - * - * - - - - - - - -
- - - - - - - - - * - - - - - - - - -
- - - - - - - - * - * - - - - - - - -
- - - - - - - * - - - * - - - - - - -
- - - - - - * - - - - - * - - - - - -
- - - - - * - - - - - - - * - - - - -
- - - - * - - - - - - - - - * - - - -
- - - * - - - - - - - - - - - * - - -
- - * - - - - - - - - - - - - - * - -
- * - - - - - - - - - - - - - - - * -
* - - - - - - - - - - - - - - - - - *

Programa la funció creu que rep 2 paràmetres n i c:
Comprova que n sigui un nombre senar positiu sinó retorna “error”.
Genera una matriu quadrada de mida n x n, amb tots el elements “ “.
Forma una creu amb el caràcter c, és a dir, tots els elements de la columna del mig han de ser el caràcter c i tots els elements de la fila del mig han de ser el caràcter c.

Exemple: creu(qua,"|"), aprofitant la mateixa matriu de l’exercici anterior, genera la sortida:
* - - - - - - - - | - - - - - - - - *
- * - - - - - - - | - - - - - - - * -
- - * - - - - - - | - - - - - - * - -
- - - * - - - - - | - - - - - * - - -
- - - - * - - - - | - - - - * - - - -
- - - - - * - - - | - - - * - - - - -
- - - - - - * - - | - - * - - - - - -
- - - - - - - * - | - * - - - - - - -
- - - - - - - - * | * - - - - - - - -
| | | | | | | | | | | | | | | | | | |
- - - - - - - - * | * - - - - - - - -
- - - - - - - * - | - * - - - - - - -
- - - - - - * - - | - - * - - - - - -
- - - - - * - - - | - - - * - - - - -
- - - - * - - - - | - - - - * - - - -
- - - * - - - - - | - - - - - * - - -
- - * - - - - - - | - - - - - - * - -
- * - - - - - - - | - - - - - - - * -
* - - - - - - - - | - - - - - - - - *
        """,
    },
}

# classes objecte ______________________________________________

# funcions ______________________________________________

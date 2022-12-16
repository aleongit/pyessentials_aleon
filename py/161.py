#Aleix Leon

#1
#Fes programa que crei un fitxer de text de nom "text.txt" i escrigui tres línies de text al fitxer
#Fes-lo usant les comandes open i close. Comprova que s'ha creat amb un editor de text, així sabràs on els guarda.

linies = ["línia1\n","línia2\n","línia3\n"]

#obrim fitxer mode escriure
f = open("text.txt", "w", encoding="utf8")

#escrivim línies a fitxer
for l in linies:
    f.writelines(l)
    
#tanquem fitxer
f.close()

print('fitxer creat!')
# la base 

# pour faire du python dans le terminal 
# >>> python
# si jamais besoin d'écrir plusieurs ligne à la fois, séparer les lignes du programme avec des ";"
# pour sortir de ce mode il faut appuyer sur : ctrl + z et faire entrée

# pour run le programme pre-fait
# faire des 'cd' jusqu'au fichier, puis écrire >> py hello(nom du fichier).py

# écrire en python
print("Hello, world")

# initiation de variable

#livre est un string
livre = "leonard"
print(livre)

#age est un integer
age = 14
print(age)

# != de la variable
print("age")

#age change de valeur et deviens un float
age = 14.5
print(age)

# moite est un boolean
moite = True
print(moite)

# type() est une méthode qui renvoi le type de la variable (dans les parenthèses)

print(type(age))

print(type(livre))

print(type(moite))

type_age = type(age)
print(type_age)

# d'après openclassroom, la convention pour appeler les variable 
# snake case = écrire tout en minuscule et utiliser des tirets du bas pour séparer les mots
# que du alphanumérique et des tirets du bas
# la variable ne doit pas commencer avec un chiffre
# par de caractères spéciaux



ligne =["pomme","poire"]

print(ligne[1])
print(ligne)

dico = {
    "tipe1": "bleu",
    "tipe2" : "rouge",
}

print(dico["tipe2"])
dico["tipe3"]="marron"

print(dico["tipe3"])
del dico["tipe2"]

print(dico)

print("tipe2" in dico)

dico["tipe2"] = "jaune"

tipepop = dico.pop("tipe2")

print("j'ai delete :",tipepop)
print(dico)

print("tipe3")
print(dico["tipe1"])

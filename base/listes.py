# les listes, c'est en incide
# ça peut être appelé comme une variable 

personnages_broken = ["katarina","yone","gankplank",14,True]

#toute la liste
print(personnages_broken)

#indice de la variable

print(personnages_broken[0])
print(personnages_broken[2])
print(personnages_broken[3])
print(personnages_broken[4])

# pas de modulo, il faut pas aller plus loin que le nombre max de la liste

# les indices négatif commence de la fin jusqu'au début

print(personnages_broken[-5])

# y'a plein de méthode pour gerer une liste
# les plus connu (d'après open classroom)

# append() pour ajouter à la fin (nom de l'ajout dans les parenthèses)

personnages_broken.append("wukong")
print(personnages_broken)

# .remove() pour enlever (si il y a plusieurs fois la même entité, ça supprime la première)

personnages_broken.remove(True)
print(personnages_broken)

# len() pour connaitre la longueur de la liste (mettre le nom de la liste dans les parenthèses)

print(len(personnages_broken))

# sort() mettre dans l'ordre (le nom de la liste dans les parenthèses)
# attention, si il y a des type de données différentes, sort ne marche pas

personnages_broken.remove(14)
personnages_broken.sort()   
print(personnages_broken)


# les tuples sont des listes qui ne bougent pas (const) écrit avec des parenthèse

pent = ("xayah","ezreal","lucian","jinx")

print(pent)

print(pent[1])

#les tuples n'ont que 2 méthodes (qui sont des méthodes communes aux listes)

# .count compte le nombre d'itération d'une valeur donné
print(pent.count("xayah"))

#index trouve la place d'une valeur donné 
#(si on écrit pent.index("xayah",2) il cherchera si il y a une valeur "xayah" après l'index [2])
# si il n'y a pas la valeur donné, retourne une erreur

print(pent.index("xayah"))


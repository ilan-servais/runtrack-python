# Fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_par_somme_voisins(lst):
    if len(lst) >= 5:
        lst[3] = lst[2] + lst[4]

# Création de la liste "L" d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Afficher la liste initiale
print(L)

# Afficher la deuxième valeur de la liste
print(L[1])

# Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
remplacer_par_somme_voisins(L)

# Afficher le tableau après la modification
print(L)

# Afficher la dernière valeur de la liste
print(L[-1])
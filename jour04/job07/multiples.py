# Liste donnée
L = [8, 24, 48, 2, 16]

# Fonction pour compter le nombre de multiples de 3
def compter_multiples_de_trois(lst):
    count = 0
    for nombre in lst:
        if nombre % 3 == 0:
            count += 1
    return count

# Appeler la fonction pour compter les multiples de 3 dans la liste
nombre_multiples_trois = compter_multiples_de_trois(L)

# Afficher le résultat
print(f"Nombre de multiples de 3 dans la liste : {nombre_multiples_trois}")
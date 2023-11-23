# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Fonction pour récupérer le maximum et le minimum des éléments de la liste
def recuperer_info_liste(lst):
    maximum = max(lst)
    minimum = min(lst)

    return maximum, minimum

# Appeler la fonction pour récupérer les informations de la liste
maximum, minimum = recuperer_info_liste(L)

# Afficher les résultats
print(f"La valeur maximale de la liste est : {maximum}")
print(f"La valeur minimale de la liste est : {minimum}")
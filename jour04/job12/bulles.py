# Fonction pour trier une liste dans l'ordre croissant (tri à bulles)
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                # Échanger les éléments s'ils ne sont pas dans l'ordre croissant
                liste[j], liste[j+1] = liste[j+1], liste[j]

# Liste donnée
L = [7, 11, 42, 39, 2]

# Appeler la fonction pour trier la liste
tri_bulles(L)

# Afficher la liste triée
print("Liste triée :", L)
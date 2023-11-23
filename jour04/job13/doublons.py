# Fonction pour supprimer les doublons d'une liste
def supprimer_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons

# Liste donnée avec doublons
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(L)

# Afficher la liste sans doublons
print("Liste sans doublons :", liste_sans_doublons)
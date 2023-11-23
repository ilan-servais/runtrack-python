# Fonction pour arrondir les nombres et les trier dans l'ordre croissant
def arrondir_et_trier(liste):
    # Arrondir les nombres dans la liste
    liste_arrondie = [int(nombre) for nombre in liste]

    # Implémenter un tri simple (tri à bulles) sans utiliser sort
    n = len(liste_arrondie)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste_arrondie[j] > liste_arrondie[j+1]:
                # Échanger les éléments s'ils ne sont pas dans l'ordre croissant
                liste_arrondie[j], liste_arrondie[j+1] = liste_arrondie[j+1], liste_arrondie[j]

    return liste_arrondie

# Liste donnée
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appeler la fonction pour arrondir et trier la liste
resultat = arrondir_et_trier(liste_nombres)

# Afficher le résultat
print("Liste arrondie et triée :", resultat)
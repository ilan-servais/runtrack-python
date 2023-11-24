def calcul_distance_toilettes(marches, hauteur_marche):
    distance_par_escalier = marches * 2 * hauteur_marche / 100  # Convertir en mètres
    distance_totale_semaine = distance_par_escalier * 5 * 7  # 5 fois par jour, 7 jours par semaine

    return distance_totale_semaine

# Demander à l'utilisateur d'entrer le nombre de marches et la hauteur de chaque marche
marches = int(input("Entrez le nombre de marches du phare : "))
hauteur_marche = float(input("Entrez la hauteur de chaque marche en cm : "))

# Appeler la fonction pour calculer la distance totale parcourue par semaine
distance_semaine = calcul_distance_toilettes(marches, hauteur_marche)

# Afficher le résultat
print(f"Pour {marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_semaine:.2f} m par semaine.")
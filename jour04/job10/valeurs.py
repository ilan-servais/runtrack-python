# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Fonction pour calculer la somme des valeurs dans l'intervalle [25, 90]
def somme_dans_intervalle(lst, borne_inf, borne_sup):
    somme = 0
    for nombre in lst:
        if borne_inf <= nombre <= borne_sup:
            somme += nombre
    return somme

# Intervalle [25, 90]
borne_inferieure = 25
borne_superieure = 90

# Appeler la fonction pour calculer la somme dans l'intervalle
resultat_somme = somme_dans_intervalle(L, borne_inferieure, borne_superieure)

# Afficher le résultat
print(f"La somme des valeurs dans l'intervalle [{borne_inferieure}, {borne_superieure}] est : {resultat_somme}")
# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Fonction pour calculer la somme des valeurs paires
def somme_valeurs_paires(lst):
    somme = 0
    for nombre in lst:
        if nombre % 2 == 0:
            somme += nombre
    return somme

# Appeler la fonction pour calculer la somme des valeurs paires dans la liste
resultat_somme = somme_valeurs_paires(L)

# Afficher le résultat
print(f"La somme des valeurs paires dans la liste est : {resultat_somme}")
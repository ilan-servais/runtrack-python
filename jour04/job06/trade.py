# Fonction pour échanger les valeurs de la première et de la dernière case
def echanger_premiere_et_derniere(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

# Création de la liste non vide
ma_liste = [1, 2, 3, 4, 5]

# Afficher la liste initiale
print(ma_liste)

# Appeler la fonction pour échanger les valeurs
echanger_premiere_et_derniere(ma_liste)

# Afficher le résultat après l'échange
print(ma_liste)
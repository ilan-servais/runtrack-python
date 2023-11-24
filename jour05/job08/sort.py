def my_sort(liste):
    coups_total = 0
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                swapped = True
                coups_total += 1

    print(f"Nombre total de coups nécessaires pour trier la liste : {coups_total}")
    return liste

# Demander à l'utilisateur d'entrer les éléments de la liste
user_input = input("Entrez les éléments de la liste séparés par des espaces : ")
ma_liste = [int(x) for x in user_input.split()]

# Appeler la fonction avec la liste de l'utilisateur
liste_triee = my_sort(ma_liste)

# Afficher la liste triée
print(f"Liste triée : {liste_triee}")

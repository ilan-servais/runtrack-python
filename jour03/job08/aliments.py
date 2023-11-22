# Définition de la fonction afficher_aliments
def afficher_aliments(type_aliment, saison):
    if type_aliment == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type_aliment == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type_aliment == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type_aliment == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée pour le type et la saison fournis.")

# Demander à l'utilisateur d'entrer un type d'aliment et une saison
type_aliment_utilisateur = input("Entrez le type d'aliment (fruits/legume) : ")
saison_utilisateur = input("Entrez la saison (hiver/ete) : ")

# Appel de la fonction avec les paramètres saisis par l'utilisateur
afficher_aliments(type_aliment_utilisateur, saison_utilisateur)
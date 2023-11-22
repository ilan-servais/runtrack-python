# Définition de la fonction afficher_signe
def afficher_signe(nombre):
    if nombre > 0:
        print(f"{nombre} est positif.")
    elif nombre < 0:
        print(f"{nombre} est négatif.")
    else:
        print(f"{nombre} est nul.")

# Demander à l'utilisateur d'entrer un nombre
nombre_utilisateur = float(input("Entrez un nombre : "))

# Appel de la fonction avec le nombre saisi par l'utilisateur
afficher_signe(nombre_utilisateur)
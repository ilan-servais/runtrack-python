# Définition de la fonction afficher_role_developpeur
def afficher_role_developpeur(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web.")
    elif langage == "python":
        print("Tu es un développeur IA.")
    elif langage == "java":
        print("Tu es un développeur logiciel.")
    elif langage == "reactjs":
        print("Tu es un développeur mobile.")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Demander à l'utilisateur d'entrer un langage
langage_utilisateur = input("Entrez un langage de programmation : ")

# Appel de la fonction avec le langage saisi par l'utilisateur
afficher_role_developpeur(langage_utilisateur)
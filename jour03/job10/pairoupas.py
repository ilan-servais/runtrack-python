# Définition de la fonction verifier_pair_impair
def verifier_pair_impair():
    try:
        # Demander à l'utilisateur d'entrer un nombre
        nombre = int(input("Entrez un nombre entier positif : "))

        # Vérifier si le nombre est un entier positif
        if nombre >= 0:
            if nombre % 2 == 0:
                print(f"{nombre} est un nombre pair.")
            else:
                print(f"{nombre} est un nombre impair.")
        else:
            print("Veuillez entrer un nombre entier positif.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Appeler la fonction
verifier_pair_impair()
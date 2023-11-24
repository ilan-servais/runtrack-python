def draw_triangle(height):
    # Vérifier si la hauteur est valide
    if height <= 0:
        print("La hauteur du triangle doit être un entier positif.")
        return

    # Dessiner le triangle
    for i in range(height):
        # Afficher les espaces avant le premier caractère '/'
        print(" " * (height - i - 1), end="")

        # Afficher le premier caractère '/'
        print("/", end="")

        # Afficher les espaces au milieu
        if i == height - 1:
            print("_" * (2 * i), end="")
        else:
            print(" " * (2 * i), end="")

        # Afficher le caractère '\'
        print("\\", end="")

        # Aller à la ligne pour la prochaine itération
        print()

# Demander à l'utilisateur de renseigner la hauteur du triangle
height = int(input("Veuillez entrer la hauteur du triangle : "))

# Appeler la fonction pour dessiner le triangle
draw_triangle(height)

def draw_rectangle(width, height):
    # Vérifier si les dimensions sont valides
    if width <= 0 or height <= 0:
        print("Les dimensions du rectangle doivent être des entiers positifs.")
        return

    # Dessiner le rectangle
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne
            print("|" + "-" * (width - 2) + "|")
        else:
            # Lignes intérieures
            print("|" + " " * (width - 2) + "|")

# Demander à l'utilisateur de renseigner les dimensions
width = int(input("Veuillez entrer la largeur du rectangle : "))
height = int(input("Veuillez entrer la hauteur du rectangle : "))

# Appeler la fonction pour dessiner le rectangle
draw_rectangle(width, height)
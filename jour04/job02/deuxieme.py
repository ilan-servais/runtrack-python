# Définition de la fonction afficher_deuxieme_element
def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    # Vérifier si la liste a au moins deux éléments
    if len(fruits) >= 2:
        print(f"Deuxième élément de la liste : {fruits[1]}")
    else:
        print("La liste ne contient pas suffisamment d'éléments.")

# Appeler la fonction
afficher_deuxieme_element()
# Définition de la fonction ajouter_mangue
def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    # Vérifier si l'index 2 est valide
    if 0 <= 2 < len(fruits):
        fruits.insert(2, "Mangue")
        return fruits
    else:
        print("L'index 2 n'est pas valide.")
        return None

# Appeler la fonction et afficher le résultat
resultat = ajouter_mangue()
if resultat is not None:
    print(resultat)
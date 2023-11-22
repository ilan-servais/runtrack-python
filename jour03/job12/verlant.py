# Définition de la fonction inverser_string
def inverser_string(chaine):
    return chaine[::-1]

# Appeler la fonction depuis le terminal avec un argument
import sys

# Récupérer l'argument fourni depuis le terminal
if len(sys.argv) > 1:
    argument = sys.argv[1]
    # Appeler la fonction avec l'argument fourni
    resultat = inverser_string(argument)
    print(f"Chaine originale : {argument}")
    print(f"Chaine inversée : {resultat}")
else:
    print("Veuillez fournir un argument (une chaîne de caractères) depuis le terminal.")
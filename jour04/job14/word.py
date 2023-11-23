# Fonction pour filtrer les mots plus longs que le chiffre donné
def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) > longueur_minimale]
    return " ".join(mots_filtres)

# Exemple d'utilisation
chiffre = 3
phrase_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

# Appeler la fonction
resultat = my_long_word(chiffre, phrase_exemple)

# Afficher le résultat
print("Output :", resultat)
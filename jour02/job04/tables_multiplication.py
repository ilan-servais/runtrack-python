# Programme pour afficher les tables de multiplication de 1 à N

try:
    # Demander à l'utilisateur de saisir un entier N
    N = int(input("Entrez un entier N supérieur à zéro : "))

    # Vérifier si N est supérieur à zéro
    if N <= 0:
        raise ValueError("N doit être un entier supérieur à zéro.")

    # Afficher les tables de multiplication
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :\n")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} * {j} = {produit}")

except ValueError as ve:
    print(f"Erreur : {ve}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
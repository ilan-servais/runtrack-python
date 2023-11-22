import sys

# Définition de la fonction calcule
def calcule(num1, operator, num2):
    try:
        result = eval(f"{num1} {operator} {num2}")
        return result
    except ZeroDivisionError:
        return "Division par zéro impossible"
    except Exception as e:
        return f"Erreur : {e}"

# Vérifier si des arguments sont passés en ligne de commande
if len(sys.argv) == 4:
    # Récupérer les paramètres depuis la ligne de commande
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    # Appeler la fonction et afficher le résultat
    resultat = calcule(num1, operator, num2)
    print(f"Résultat de l'opération : {resultat}")
else:
    print("Usage: python chemin/vers/le/fichier/calcule_function.py <nombre1> <opérateur> <nombre2>")

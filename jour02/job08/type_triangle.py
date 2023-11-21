# Programme pour déterminer le type de triangle

def determiner_type_triangle(a, b, c):
    # Vérifier si les longueurs forment un triangle
    if a + b > c and a + c > b and b + c > a:
        # Vérifier le type de triangle
        if a == b == c:
            return "Equilatéral"
        elif a == b or b == c or a == c:
            # Vérifier s'il s'agit d'un triangle rectangle isocèle
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Rectangle isocèle"
            else:
                return "Isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle"
        else:
            return "Quelconque"
    else:
        return "Impossible de former un triangle"

# Demander à l'utilisateur les longueurs a, b, c
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Appeler la fonction pour déterminer le type de triangle
type_triangle = determiner_type_triangle(a, b, c)

# Afficher le résultat
print(f"Le triangle est de type : {type_triangle}")

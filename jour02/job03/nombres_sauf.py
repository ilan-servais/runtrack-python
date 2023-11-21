# Programme pour afficher tous les nombres de 0 à 100 sauf 26, 37, et 88

# Boucle for pour parcourir les nombres de 0 à 100 inclus
for nombre in range(101):
    # Exclure les nombres spécifiques (26, 37, 88)
    if nombre not in [26, 37, 88]:
        # Afficher chaque nombre dans le terminal
        print(nombre)
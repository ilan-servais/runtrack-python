# Programme pour afficher l'alphabet dans le terminal

# La fonction ord() renvoie le code ASCII d'un caractère
# La fonction chr() renvoie le caractère correspondant à un code ASCII

# Début de la boucle for, de la lettre 'a' à 'z'
for lettre in range(ord('a'), ord('z') + 1):
    # Afficher la lettre correspondante
    print(chr(lettre), end=' ')

# Saut de ligne à la fin
print()

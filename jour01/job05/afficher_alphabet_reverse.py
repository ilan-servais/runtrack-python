# Programme pour afficher l'alphabet à l'envers dans le terminal

# La fonction ord() renvoie le code ASCII d'un caractère
# La fonction chr() renvoie le caractère correspondant à un code ASCII

# Début de la boucle for, de la lettre 'z' à 'a' (en sens inverse)
for lettre in range(ord('z'), ord('a') - 1, -1):
    # Afficher la lettre correspondante
    print(chr(lettre), end=' ')

# Saut de ligne à la fin
print()

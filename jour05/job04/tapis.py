def afficher_tapis(n):
    print('+' + '-' * (n+2) + '+')
    for i in range(n+1):
        print('|' + '#' * i + ' ' + '#' * (n - i) + '|')
    print('+' + '-' * (n+2) + '+')

taille = int(input("Entrez la taille du tapis : "))
afficher_tapis(taille)

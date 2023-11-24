def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_sup = (note // 5 + 1) * 5
            if multiple_de_5_sup - note < 3:
                notes_arrondies.append(multiple_de_5_sup)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Entrée: Liste de notes initiales
notes_initiales = [83, 72, 65, 40, 92, 77, 88, 54]

# Utilisation de la fonction pour obtenir la liste de notes arrondies
notes_arrondies = arrondir_notes(notes_initiales)

# Affichage des résultats
for i in range(len(notes_initiales)):
    print(f"Note initiale : {notes_initiales[i]}, Note arrondie : {notes_arrondies[i]}")
# Programme de simulation financière pour un investissement

# Initialiser les variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Afficher le gain annuel en fonction du taux de rendement initial
gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print(f"Gain annuel initial : {gain_annuel:.2f} euros")

# Augmenter le capital de 5 000 euros et le taux de rendement de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calculer le nouveau gain annuel
nouveau_gain_annuel = (montant_initial * taux_rendement_annuel) / 100
print(f"Nouveau gain annuel : {nouveau_gain_annuel:.2f} euros")

# Retirer 10% du montant total, le rendement diminue de 1%
montant_initial *= 0.90  # Retirer 10%
taux_rendement_annuel -= 1

# Calculer le montant final de l'investissement et le nouveau gain
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
nouveau_gain = montant_final - montant_initial

# Afficher le montant final et le nouveau gain
print(f"Montant final de l'investissement : {montant_final:.2f} euros")
print(f"Nouveau gain : {nouveau_gain:.2f} euros")
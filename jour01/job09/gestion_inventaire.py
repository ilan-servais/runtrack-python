# Programme de gestion d'inventaire

# Définir les variables du produit initial
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_en_stock = 50

# Afficher les informations du produit de manière formatée
print("Informations du produit:")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités")
print()

# Ajouter des produits en stock
quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock += quantite_achetee

# Mettre à jour le prix du produit en raison de l'inflation (10% d'augmentation)
prix_unitaire *= 1.10

# Afficher à nouveau les informations du produit après la mise à jour
print("Informations mises à jour du produit:")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire : {prix_unitaire:.2f} euros")
print(f"Nouvelle quantité en stock : {quantite_en_stock} unités")
print("Bienvenue dans le programme")

# Liste pour stocker les articles
articles = []

while True:
    options = ["1) Ajouter un article", "2) Voir les articles", "3) Supprimer un article", "4) Quitter"]
    for option in options:
        print(option)
    
    # Demande de type d'opération
    print("Choisissez une option ou quittez le programme")
    demande = input("=> ")

    # Quitter le programme
    if demande == "4":
        print("Merci d'avoir utilisé le programme. Au revoir!")
        break

    # Ajouter un article
    if demande == "1":
        try:
            nom = input("Donnez un nom à l'article: ")
            quantite = int(input("La quantité: "))
            unite = input("Choisissez une unité (Kg, Litre, To) : ")
        except ValueError:
            print("Veuillez entrer des nombres valides pour la quantité.")
            continue
        
        articles.append({'nom': nom, 'quantite': quantite, 'unite': unite})
        print(f"L'article {nom} a été ajouté avec succès!")
        continue
    
    # Voir les articles
    if demande == "2":
        if not articles:
            print("Aucun article à afficher.")
        else:
            print("Les articles :")
            for index, article in enumerate(articles, start=1):
                print(f"{index}) Nom: {article['nom']}, Quantité: {article['quantite']} {article['unite']}")
                print("_________________________________________")
        continue
    
    # Supprimer un article
    if demande == "3":
        if not articles:
            print("Aucun article à supprimer.")
        else:
            try:
                index_to_remove = int(input("Entrez le numéro de l'article à supprimer: ")) - 1
                if 0 <= index_to_remove < len(articles):
                    removed_article = articles.pop(index_to_remove)
                    print(f"L'article {removed_article['nom']} a été supprimé avec succès!")
                else:
                    print("Numéro d'article invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        continue

    # Choix invalide
    if demande not in ['1', '2', '3', '4']:
        print(f"L'option {demande} n'est pas disponible.")
        print("_________________________________________")
        print("")
        continue

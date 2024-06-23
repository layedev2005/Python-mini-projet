print("Choisir votre opération")

city = input("Entrez le pays: ")
initial_population = int(input("Entrez la population initiale: "))
birth = int(input("Nombre de naissances: "))
death = int(input("Nombre de décès: "))

# Calcul de l'accroissement naturel
natural_increase = birth - death

# Calcul de l'accroissement naturel en pourcentage
natural_increase_percentage = (natural_increase / initial_population) * 100

# Affichage des résultats
print(f"\nRésultats pour {city}:")
print(f"Accroissement naturel: {natural_increase} personnes")
print(f"Accroissement naturel en pourcentage: {natural_increase_percentage:.2f}%")

if natural_increase > 0:
    print(f"Le {city} a une croissance naturelle positive :)")
else:
    print(f"Le {city} a une décroissance naturelle :(")

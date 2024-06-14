print("Bienvenue! Quel type d'opération voulez-vous faire?")

choic_opperation = ["1: addition", "2: soustraction", "3: multiplication", "4: division"]
for i in choic_opperation:
    print(i)

while True:
    demande = input("Opération (ou 'q' pour quitter) : ")

    if demande == 'q':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break

    if demande not in ['1', '2', '3', '4']:
        print("Choix invalide. Veuillez sélectionner une option valide.")
        continue

    try:
        a = float(input("Entrez le premier nombre: "))
        b = float(input("Entrez le deuxième nombre: "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        continue

    class Calc:
        @staticmethod
        def addition(a, b):
            return a + b

        @staticmethod
        def soustraction(a, b):
            return a - b

        @staticmethod
        def division(a, b):
            if b == 0:
                return "Erreur: Division par zéro!"
            return a / b

        @staticmethod
        def multiplication(a, b):
            return a * b

    if demande == '1':
        result = Calc.addition(a, b)
        operation = "addition"
    elif demande == '2':
        result = Calc.soustraction(a, b)
        operation = "soustraction"
    elif demande == '3':
        result = Calc.multiplication(a, b)
        operation = "multiplication"
    elif demande == '4':
        result = Calc.division(a, b)
        operation = "division"

    print(f"Le résultat de la {operation} de {a} et {b} est: {result}")
    print(f"result {operation} de baba top = {result}")
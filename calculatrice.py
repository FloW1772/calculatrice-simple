def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"

print("Sélectionnez une opération :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Entrez votre choix (1/2/3/4): ")

nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

if choix == '1':
    print(nombre1, "+", nombre2, "=", addition(nombre1, nombre2))
elif choix == '2':
    print(nombre1, "-", nombre2, "=", soustraction(nombre1, nombre2))
elif choix == '3':
    print(nombre1, "*", nombre2, "=", multiplication(nombre1, nombre2))
elif choix == '4':
    print(nombre1, "/", nombre2, "=", division(nombre1, nombre2))
else:
    print("Choix invalide")

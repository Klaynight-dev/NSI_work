def rendu(monnaie, rendre, n=None, liste=None):
    if n is None:
        n = 0
    if liste is None:
        liste = []
    if rendre == 0:
        return liste
    if n < len(monnaie):
        diviser = rendre // monnaie[n]
        for _ in range(diviser):
            liste.append(monnaie[n])
            rendre -= monnaie[n]
    return rendu(monnaie, rendre, n + 1, liste)

def verif(rendre):
    rendre = int(rendre)  # Convertir la saisie en nombre (peut être un entier ou un nombre à virgule)
    assert rendre != 0, "Le nombre doit être différent de zéro"
    assert rendre >= 0, "Le nombre ne peut être négatif, il doit être supérieur à 0"
    print("Le nombre est valide :", rendre)

monnaie = [100, 50, 20, 10, 5, 2, 1]
rendre = int(input("Veuillez entrer un nombre : "))

verif(rendre)

resultat = rendu(monnaie, rendre)
print(resultat)  # Rendre 54 avec les unités monétaires données

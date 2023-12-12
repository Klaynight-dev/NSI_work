def rendre_monnaie(montant, valeurs, index=0):
    assert montant_a_rendre>0, "Veuillez entrer un nombre positif !"
    if montant == 0:
        return []
    
    if index >= len(valeurs):
        return None

    valeur = valeurs[index]
    max_pieces = montant // valeur

    meilleure_solution = None

    for nombre_de_pieces in range(max_pieces, -1, -1):
        reste = montant - nombre_de_pieces * valeur
        solution_partielle = rendre_monnaie(reste, valeurs, index + 1)

        if solution_partielle is not None:
            pieces = [valeur] * nombre_de_pieces
            solution = pieces + solution_partielle

            if meilleure_solution is None or len(solution) < len(meilleure_solution):
                meilleure_solution = solution

    return meilleure_solution

montant_a_rendre = int(input("Veuillez enter un nombre : "))
valeurs_disponibles = [100, 50, 20, 10, 5, 2, 1]

solution = rendre_monnaie(montant_a_rendre, valeurs_disponibles)

if solution is not None:
    print("Solution gloutonne optimale :")
    print(solution)
else:
    print("Aucune solution trouvée.")

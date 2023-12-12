def multiple(nombre):
    if nombre % 13 == 0:
        return True
    else:
        return False

# Exemples d'utilisation de la fonction
resultat1 = est_multiple_de_13(26)  # True, car 26 est un multiple de 13 (2 * 13)
resultat2 = est_multiple_de_13(7)   # False, car 7 n'est pas un multiple de 13

print(resultat1)
print(resultat2)

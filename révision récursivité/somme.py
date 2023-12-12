def sommes(n):
    """Permet de calculer la somme de n et de tout les nombres plus petit."""
    if n==0:
    # Condition d'arret
        return n
    else:
    # Appel récursif
        return n+sommes(n-1)

# 982 est le nombre maximum de la capacité récursive.
print(sommes(982))
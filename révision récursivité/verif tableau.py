def recherche_recursive(valeur, tableau=[3, 7, 11, 5, 9]):
    """Verifie via la récursivité si un nombre est dans le tableau"""
    if tableau:
        if tableau[0] == valeur:
            return True
        return recherche_recursive(valeur, tableau[1:])
    return False

valeur_recherchee = 56

resultat = recherche_recursive(valeur_recherchee)
if resultat:
    print(f"La valeur {valeur_recherchee} est présente dans le tableau.")
else:
    print(f"La valeur {valeur_recherchee} n'est pas présente dans le tableau.")
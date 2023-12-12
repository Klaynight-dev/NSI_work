def chiffre_romain_vers_nombre(chiffre_romain, cr={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}):
    if chiffre_romain.isnumeric():
        nombre = int(chiffre_romain)
        if 1 <= nombre <= 3999:
            valeurs = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                       (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                       (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
            chiffre_romain = ''
            for valeur, symbole in valeurs:
                while nombre >= valeur:
                    nombre -= valeur
                    chiffre_romain += symbole
            return chiffre_romain
        else:
            return "Le nombre doit être compris entre 1 et 3999 pour être converti en chiffre romain."
    else:
        if len(chiffre_romain) == 0:
            return 0
        if len(chiffre_romain) == 1:
            return cr[chiffre_romain[0]]
        if cr[chiffre_romain[0]] < cr[chiffre_romain[1]]:
            return cr[chiffre_romain[1]] - cr[chiffre_romain[0]] + chiffre_romain_vers_nombre(chiffre_romain[2:], cr)
        return cr[chiffre_romain[0]] + chiffre_romain_vers_nombre(chiffre_romain[1:], cr)

# Exemple d'utilisation avec un nombre entier ou un chiffre romain
entree = "CMXCIX"
resultat = chiffre_romain_vers_nombre(entree)
if resultat == entree:
    print(f"{entree} = {resultat}")
else:
    print(f"{entree} en chiffre romain = {resultat}")

entree_nombre = "2023"

chiffre_romain="MMMDXLII"
resultat=chiffre_romain_vers_nombre(chiffre_romain)
print(f"{chiffre_romain} = {resultat}")
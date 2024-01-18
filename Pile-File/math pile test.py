class MaPile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if self.est_vide():
            return None
        return self.elements.pop()

    def sommet(self):
        if self.est_vide():
            return None
        return self.elements[-1]


def parentheses_equilibrees(expression):
    pile = MaPile()

    for caractere in expression:
        if caractere == '(':
            pile.empiler(caractere)
        elif caractere == ')':
            if pile.est_vide() or pile.sommet() != '(':
                return False
            pile.depiler()

    return pile.est_vide()


# Exemples d'expressions mathématiques
expressions = [
    "((2 + 3) * (4 - 1))",
    "((2 + 3) * (4 - 1)"
]

for expression in expressions:
    est_equilibree = parentheses_equilibrees(expression)
    if est_equilibree:
        print(f"L'expression '{expression}' a des parenthèses équilibrées.")
    else:
        print(f"L'expression '{expression}' n'a pas de parenthèses équilibrées.")

from random import randint
class Pile:
    def __init__(self):
        self.elements = []  # Utilisation d'une liste pour stocker les éléments de la pile

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)  # Ajouter un élément à la fin de la liste

    def depiler(self):
        if self.est_vide():
            return None
        return self.elements.pop()  # Retirer et renvoyer le dernier élément de la liste

    def sommet(self):
        if self.est_vide():
            return None
        return self.elements[-1]  # Renvoyer le dernier élément de la liste sans le retirer

    def taille(self):
        return len(self.elements)  # Renvoyer la taille de la pile

# Création d'une pile
pile = Pile()

for piles in range(10):
    pile.empiler(randint(10,50))

# Vérifier le sommet de la pile
print("Sommet de la pile :", pile.sommet())  # Output : Sommet de la pile : 15

# Dépiler un élément
element_depile = pile.depiler()
print("Élément dépilé :", element_depile)  # Output : Élément dépilé : 15

# Vérifier à nouveau le sommet de la pile
print("Nouveau sommet de la pile :", pile.sommet())  # Output : Nouveau sommet de la pile : 10

# Taille de la pile
print("Taille de la pile :", pile.taille())  # Output : Taille de la pile : 2

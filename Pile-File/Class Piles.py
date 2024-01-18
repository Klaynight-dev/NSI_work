from random import randint
class Pile:
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

    def taille(self):
        return len(self.elements)
    
    def afficher(self):
        return self.elements

pile = Pile()

for piles in range(10):
    pile.empiler(randint(10,50))

print(f"Voici la pile de départ : \n{pile.afficher()}")
print("\nSommet de la pile :", pile.sommet())

element_depile = pile.depiler()
print("\nÉlément dépilé :", element_depile)
print(f"\nVoici la liste actuel : \n{pile.afficher()}")

print("\nNouveau sommet de la pile :", pile.sommet())

print("\nTaille de la pile :", pile.taille()) # output = 9

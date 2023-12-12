from random import randint

class MaPile:
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

    def max(self):
        if self.est_vide():
            return None
        return max(self.elements)  # Renvoyer la valeur maximale de la pile


# Fonction pour séparer une pile en piles de nombres pairs et impairs
def separer_piles(pile):
    pile_pairs = MaPile()
    pile_impairs = MaPile()
    temp_pile = MaPile()

    # Transférer les éléments dans une pile temporaire tout en conservant l'ordre initial
    while not pile.est_vide():
        temp_pile.empiler(pile.depiler())

    # Séparer les éléments pairs et impairs dans les piles correspondantes
    while not temp_pile.est_vide():
        element = temp_pile.depiler()
        if element % 2 == 0:  # Si le nombre est pair
            pile_pairs.empiler(element)
        else:
            pile_impairs.empiler(element)

    return pile_pairs, pile_impairs


# Création d'une pile initiale
pile_initiale = MaPile()

for piles in range(10):
    pile_initiale.empiler(randint(10, 50))
    print(pile_initiale.sommet())

# Obtenir la valeur maximale de la pile initiale
print("\nValeur maximale de la pile initiale:", pile_initiale.max())

# Séparation de la pile initiale en piles de nombres pairs et impairs
pile_pairs, pile_impairs = separer_piles(pile_initiale)

# Affichage des piles de nombres pairs et impairs
print("\nPile des nombres pairs:")
liste = []
while not pile_pairs.est_vide():
    liste.append(pile_pairs.depiler())
print(liste)
liste = []
print("\nPile des nombres impairs:")
while not pile_impairs.est_vide():
    liste.append(pile_impairs.depiler())
print(liste)
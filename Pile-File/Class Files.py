from random import randint
class File:
    def __init__(self):
        self.elements = []
        
    def est_vide(self):
        return len(self.elements) == 0

    def emfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        return self.elements.pop(0) if self.est_vide()!=True else None

    def sommet(self):
        return self.elements[0] if self.est_vide()!=True else None

    def taille(self):
        return len(self.elements)

    def afficher(self):
        return self.elements


file = File()

for files in range(10):
    file.emfiler(randint(10,50))

print(f"Voici la pile de départ : \n{file.afficher()}")
print("Sommet de la file :", file.sommet())

element_defile = file.defiler()
print("Élément dépilé :", element_defile)
print(f"\nVoici la liste actuel : \n{file.afficher()}")

print("\nNouveau sommet de la file :", file.sommet())

print("\nTaille de la file :", file.taille()) # output = 9


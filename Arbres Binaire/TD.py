class Noeud:
    def __init__(self, nom):
        self.nom = nom
        self.filsG = None
        self.filsD = None
    
    def insertGauche(self, valeur):
        if self.filsG == None:
            self.filsG=Noeud(valeur)
        
        else:
            nouvelleValeur=Noeud(valeur)
            nouvelleValeur.filsG=self.filsG
            self.filsG = nouvelleValeur
            
    def insertDroit(self, valeur):
        if self.filsD == None:
            self.filsD=Noeud(valeur)
        
        else:
            nouvelleValeur=Noeud(valeur)
            nouvelleValeur.filsG=self.filsD
            self.filsD = nouvelleValeur
    
    def afficher(self, prefix=''):
        print(prefix + '|___' + self.nom)
        if self.filsG:
            self.filsG.afficher(prefix + '|   ')
        if self.filsD:
            self.filsD.afficher(prefix + '|   ')
            
    def afficher_tuple(self, arbre):
        if arbre != None:
            return (self.get_valeur(),
                    self.filsG.afficher_tuple(self.get_gauche()) if self.filsG != None else None,
                    self.filsD.afficher_tuple(self.get_droit())if self.filsD != None else None)

    def get_valeur(self):
        return self.nom
    
    def get_gauche(self):
        if self.filsG.nom != None:
            return self.filsG.nom
        else:
            return None

    def get_droit(self):
        if self.filsD.nom != None:
            return self.filsD.nom
        else:
            return None
    
Arbre=Noeud('A')

Arbre.insertGauche('B')
Arbre.insertDroit('C')

Arbre.filsG.insertGauche('D')
Arbre.filsG.insertDroit('E')

Arbre.filsG.filsD.insertGauche('F')
Arbre.filsG.filsD.insertDroit('G')

print(Arbre.afficher_tuple('A'))

print(Arbre.get_valeur(),'\n')
print(Arbre.get_gauche(),'\n')
print(Arbre.get_droit(),'\n')
Arbre.afficher()
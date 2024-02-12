#tools.py

class Noeud:
    def __init__(self, val=None, nom=None):
        self.filsG = None
        self.filsD = None
        self.valeur = val
        self.nom = f"{nom}-{val}"
        self.lettre=nom
        
    def insertGauche(self, valeur, nom=None):
        if self.filsG == None:
            self.filsG=Noeud(nom,valeur.get_nom)
        
        else:
            nouvelleValeur=Noeud(valeur,valeur)
            nouvelleValeur.filsG=self.filsG
            self.filsG = nouvelleValeur
            
    def insertDroit(self, valeur, nom=None):
        if self.filsD == None:
            self.filsD=Noeud(nom,valeur.get_nom())
        
        else:
            nouvelleValeur=Noeud(valeur,valeur)
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

    def get_nom(self):
        return self.nom
    
    def get_valeur(self):
        return self.valeur
    
    def get_lettre(self):
        return self.lettre
    
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
        
    def afficher_nombre_apparitions(self, prefix=''):
        total_apparitions = self.valeur

        if self.filsG:
            total_apparitions += str(self.filsG.afficher_nombre_apparitions(prefix + ' -> ' + self.lettre + ' | '))

        if self.filsD:
            total_apparitions += str(self.filsD.afficher_nombre_apparitions(prefix + ' -> '))

        if self.filsG:
            print(prefix + f'{self.valeur}')
        else:
            print(prefix + f'{self.lettre} | {self.valeur}')

        return total_apparitions

#<==================================================================================>

def find(liste, search):
    for i in liste:
        if i == search:
            return True
    return False
class Noeud:
    def __init__(self, g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self,):
        return self.gauche is None and self.droite is None
    
def ixpressions_infixe(e):
    s=''
    if e.gauche is not None:
        s='('+s+ixpressions_infixe(e.gauche)
    s=s+str(e)
    if e.droit is not None:
        s=s+ixpressions_infixe(e.droit)+')'
    
    return s

e=Noeud(
    Noeud(
        Noeud(None,3,None),
        '*',
        Noeud(
            Noeud(None,8,None),
            '+',
            Noeud(None, 7,None))),
    '-',
    Noeud(
        Noeud(None,2,None),
        '+',
        Noeud(None,1,None)))

print(ixpressions_infixe(e))
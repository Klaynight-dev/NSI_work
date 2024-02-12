#main.py

from tools import find, Noeud

class arbre:
    def __init__(self, mot):
        self.mot=mot
        self.dico={}
        self.count_lettre = []
        
        self.__init_mot__()
        
    def __init_mot__(self):
        liste=[]
        for lettre in self.mot:
            if not find(liste, lettre):
                liste.append(lettre)
                obj=Noeud(lettre, self.mot.count(lettre))
                self.count_lettre.append(obj)

    def mini(self):
        mini=None
        for obj in self.count_lettre:
            if mini==None:
                mini = obj.valeur
                mini_save=obj
            if mini>obj.valeur:
                mini = obj.valeur
                mini_save=obj
        self.mini1=mini_save
        self.count_lettre.pop(self.count_lettre.index(self.mini1))
    
    def fusion(self):
        while len(self.count_lettre) > 1:
            self.mini()
            self.mini2=self.mini1
            self.mini()
        
            val = self.mini2.valeur + self.mini1.valeur
        
            obj=Noeud(val, val)
            obj.insertDroit(self.mini2 if self.mini2.valeur >= self.mini1.valeur else self.mini1)
            obj.insertGauche(self.mini2 if self.mini2.valeur <= self.mini1.valeur else self.mini1)
            
            self.count_lettre.append(obj)
        
        self.racine = self.count_lettre[0]
        self.racine.afficher()
        

mot = "alibabas"

arbre = arbre(mot)
arbre.fusion()

print('Total:', arbre.racine.afficher_nombre_apparitions())
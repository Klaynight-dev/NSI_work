from random import randint
from tabulate import tabulate # pour afficher sous forme de tableau

class Carré:
    def __init__(self,n,liste):
        self.nbr=n
        self.table=[[17, 24,  1,  8, 15],
    [23,  5,  7, 14, 16],
    [ 4,  6, 13, 20, 22],
    [10, 12, 19, 21,  3],
    [11, 18, 25,  2,  9]]
# 
#         for ligne in range(n):
#             sTable=[]
#             for colonne in range(n):
#                 sTable.append(randint(0,9))
#             self.table.append(sTable)
            
    def affiche(self):
        print(tabulate(self.table, tablefmt='grid'))
            
    def sommeLigne(self):
        self.sommeLigneN=[]
        for ligne in self.table:
            somme=0
            for nbr in ligne:
                somme+=nbr
            self.sommeLigneN.append(somme)
        
#         self.AfficheSommeLigne()
            
    def sommeColonne(self):
        self.sommeColonneN=[]
        for ligne in range(len(self.table)):
            somme=0
            for nbr in range(len(self.table)):
                somme+=self.table[nbr][ligne]
            self.sommeColonneN.append(somme)
        
#         self.AfficheSommeColonne()
            
    def AfficheSommeLigne(self):
        for i in range(len(self.sommeLigneN)):
            print(f"Ligne {i+1} = {self.sommeLigneN[i]}")
        
    def AfficheSommeColonne(self):
        for i in range(len(self.sommeLigneN)):
            print(f"Colonne {i+1} = {self.sommeColonneN[i]}")
            
    def TestMagic(self):
        # Vérification de la somme des lignes et des colonnes
        sum_diagonal1 = 0
        sum_diagonal2 = 0
        magic_sum = sum(self.table[0])

        for i in range(self.nbr):
            if sum(self.table[i]) != magic_sum:
                return False

            column_sum = sum(row[i] for row in self.table)
            if column_sum != magic_sum:
                return False

            sum_diagonal1 += self.table[i][i]
            sum_diagonal2 += self.table[i][self.nbr - 1 - i]

        # Vérification des deux diagonales
        if sum_diagonal1 != magic_sum or sum_diagonal2 != magic_sum:
            return False

        return True
    
    def CaseAutour(self, x, y):
        cases_autour = []
        for i in range(max(0, x - 1), min(self.nbr, x + 2)):
            row = []
            for j in range(max(0, y - 1), min(self.nbr, y + 2)):
                if i != x or j != y:
                    row.append(self.table[i][j])
                else:
                    row.append("X")  # Marquer la case actuelle

            cases_autour.append(row)

        print(tabulate(cases_autour, tablefmt='grid'))
        

true=False
while true==False:
    c=Carré(5, [])
#     c.affiche()
    c.sommeLigne()
    c.sommeColonne()
#     print()
    true = c.TestMagic()
    
if true==True:
    c.affiche()
    x, y = 2, 2
    c.CaseAutour(x, y)
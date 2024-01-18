import networkx as nx
import matplotlib.pyplot as plt

class Noeud:
    def __init__(self, nom):
        self.nom = nom
        self.filsG = None
        self.filsD = None
        self.G = nx.Graph()
        self.G.add_node(self.get_valeur())
    
    def insertGauche(self, valeur):
        if self.filsG == None:
            self.filsG = Noeud(valeur)
        else:
            nouvelleValeur = Noeud(valeur)
            nouvelleValeur.filsG = self.filsG
            self.filsG = nouvelleValeur
            
        if self.get_gauche() != None:
            self.G.add_node(self.get_gauche())
            self.G.add_edge(self.get_valeur(), self.get_gauche())

    def insertDroit(self, valeur):
        if self.filsD == None:
            self.filsD = Noeud(valeur)
        else:
            nouvelleValeur = Noeud(valeur)
            nouvelleValeur.filsG = self.filsD
            self.filsD = nouvelleValeur
        
        if self.get_droit() != None:
            self.G.add_node(self.get_droit())
            self.G.add_edge(self.get_valeur(), self.get_droit())
    
    def get_valeur(self):
        return self.nom
    
    def get_gauche(self):
        if self.filsG != None:
            return self.filsG.nom
        else:
            return None

    def get_droit(self):
        if self.filsD != None:
            return self.filsD.nom
        else:
            return None
        
    def add_subnodes(self, node):
        if node.nom is not None:
            self.G.add_node(node.get_valeur())
            if node.get_gauche() is not None:
                self.G.add_edge(node.get_valeur(), node.get_gauche())
                self.add_subnodes(node.filsG)
            if node.get_droit() is not None:
                self.G.add_edge(node.get_valeur(), node.get_droit())
                self.add_subnodes(node.filsD)
    
    def get_visu(self):
        self.add_subnodes(self)
        self.pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, self.pos)
        nx.draw_networkx_edges(self.G, self.pos)
        nx.draw_networkx_labels(self.G, self.pos)

        plt.show()

racine = Noeud("A")
racine.insertGauche("B")
racine.insertDroit("C")
racine.filsG.insertDroit("D")
racine.filsG.insertGauche("E")

racine.get_visu()

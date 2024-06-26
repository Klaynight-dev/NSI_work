from pile import Pile
from time import sleep
from os import name, system
import pyxel


class Jeu:
    """
    Objet représentant le jeu des Tours de Hanoï.
    Pour démarrer le jeu : appeler la méthode .start()
    """

    def __init__(self, n=5, refresh_rate=30):
        """
        Créer une instance de jeu des tours de hanoi.
        :param int n: Nombre de plateaux (par défaut 5)
        :param int refresh_rate: Nombre de rafraichisements par seconde
        """
        self.n = n
        self.tour_selected = 1
        self.fps = refresh_rate
        self.focus = False
        self.current_frame = 0
        self.bot = False
        self.action = 0
        self.instructions = []
        self.depart = -1
        self.coup = 0
        self.tours = (Pile(), Pile(), Pile())
        for i in range(n):
            self.tours[0].empiler(n-i)

    def deplace(self, depart: int, arrivee: int):
        """
        Déplacer un plateau de la tour {depart} à la tour {arrivee}.
        Les tours sont numérotées de 1 à 3.
        :param int depart: Numéro de la tour de depart
        :param int arrivee: Numéro de la tour d'arrivée
        """
        if self.tours[depart-1].taille() == 0: return
        if self.tours[arrivee-1].content:
            if self.tours[depart-1].content[-1] > self.tours[arrivee-1].content[-1]:
                
                print("""
          ===============
        MOUVEMENT IMPOSSIBLE
          ===============
                """)
                sleep(1)
                return
        plateau = self.tours[depart-1].depiler()
        self.tours[arrivee-1].empiler(plateau)

    def __str__(self) -> str:
        """
        Renvoie un affiche textuelle de l'état du jeu.
        """
        res = ""
        i = 0
        for tour in self.tours:
            a = tour.content.copy()
            a.reverse()
            for item in a:
                plateau = ""
                for j in range(self.n-item):
                    plateau += " "
                for j in range(item):
                    plateau += "=="
                res += f"\t{plateau}\n"
            i += 1
            res += f"   \##### tour {i} #####/\n\n"
        return res

    def update(self):
        """
        Méthode appelée par Pyxel à chaque rafraichisement de la fenêtre.
        """
        if self.bot:
            self.current_frame += 1
            if self.current_frame % self.fps*2 == 0:
                if self.action > len(self.instructions)-1:
                    return
                self.deplace(self.instructions[self.action][0], self.instructions[self.action][1])
                self.action += 1
            return
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.tour_selected = 3 if self.tour_selected == 3 else self.tour_selected + 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.tour_selected = 1 if self.tour_selected == 1 else self.tour_selected - 1
        elif pyxel.btnp(pyxel.KEY_RETURN):
            if self.focus:
                self.focus = False
                self.deplace(self.depart, self.tour_selected)
                self.depart = -1
                return
            self.focus = True
            self.depart = self.tour_selected
    
    def solver(self, k, source=1, auxiliary=2, destination=3) -> list:
        """
        Méthode récursive retournant une liste
        indiquant les mouvements nécessaires 
        pour résoudre la partie.
        :param int k: Nombre de disques en jeu.
        :param int source: Numéro de la première tour
        :param int auxiliary: Numéro de la seconde tour
        :param int destination: Numéro de la troisième tour
        """
        if k == 1:
            self.instructions += [[source, destination]]
            return
        self.solver(k-1, source, destination, auxiliary)
        self.instructions += [[source, destination]]
        self.solver(k-1, auxiliary, source, destination)

    def draw(self):
        """
        Méthode appelée par Pyxel à chaque rafraichisement de la fenêtre
        qui a pour but de gérer l'affichage des composants.
        """
        pyxel.cls(7)
        i = 0
        for tour in self.tours:
            i+=1
            j = 0
            pyxel.rect(800*i/4-185/2, 325, 185, 15, 8 if self.tour_selected == i and j == len(tour.content) else 0)
            for plateau in tour.content:
                j+=1
                clr = 13
                if self.tour_selected == i and j == len(tour.content) : clr = 8
                if self.depart == i and j == len(tour.content): clr = 11
                pyxel.rect(800*i/4-(50+(plateau-1)*30)/2, 300-25*(j-1), 50+(plateau-1)*30, 15, clr) # petite formule (dont je ne suis pas peu fier) qui permet de positioner les plateaux de manière centrée sur les piquets sans utilser un seul if statement.
        
    def start(self):
        """
        Méthode qui permet de démarrer le jeu et
        ainsi proposer le choix entre lancer le jeu avec
        une TUI ou avec une GUI.
        """
        choix = input("1. Lancer le jeu en console \n2. Lancer le jeu avec une GUI\n3. Lancer la résolution automatique\n>>> ")
        if choix == '1':
            self.console()
        elif choix == '2':
            self.gui()
        elif choix == '3':
            self.bot = True
            
            print("""
            Calcul des actions a effectuer ...
            """)
            self.solver(self.n)
            
            self.gui()
        else:
            self.start()

    def gui(self):
        """
        Méthode permettant de lancer le jeu avec une GUI (Graphical User Interface).
        :param bool mouse: Active ou désactive l'affichage de la souris.
        """
        pyxel.init(800, 500, "Tour de Hanoi", self.fps, display_scale=1)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
    
    def console(self):
        """
        Méthode permettant de lancer le jeu en console.
        """
        while self.tours[2].taille() < self.n:
            
            print(self)
            arr = input("déplacer l'anneau de la tour n° ")
            dep = input("vers la tour n° ")
            nb = ["1", "2", "3"]
            if arr in nb and dep in nb:
                self.deplace(int(arr), int(dep))
                self.coup += 1
        print(f"""
        ============
        -- FIN DU JEU --
           en {self.coup} coups
        ============
        """)


# Lance une instance du jeu.
if __name__ == "__main__":
    jeu = Jeu(n=5)
    jeu.start()

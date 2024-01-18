import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Ma fenetre")

        # activation du suivi du mouvement de la souris
        self.setMouseTracking(True)
        
    def mouseMoveEvent(self,event):
        print("position = " + str(event.x()) + " " + str(event.y()))
            
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
fen = Fenetre()
fen.show()

app.exec_()
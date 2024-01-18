import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QHBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.etat= False

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Exemple de base')

        # Créer un layout horizontal
        self.layout = QHBoxLayout()

        # Ajouter les widgets au layout
        self.lbl = QLabel('Texte', self)
        self.layout.addWidget(self.lbl)

        self.edit = QLineEdit(self)
        self.layout.addWidget(self.edit)

        self.button = QPushButton('Imprimer', self)
        self.button.clicked.connect(self.print_text)
        self.layout.addWidget(self.button)

        self.btn = QPushButton('Bouton', self)
        self.btn.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.btn)
        
        self.cb = QCheckBox('Case à cocher', self)
        self.cb.clicked.connect(self.etat)
        self.layout.addWidget(self.cb)

        # Appliquer le layout au widget principal
        self.setLayout(self.layout)

        self.show()
    
    def on_button_click(self):
        print('Button clicked!')
    
    def etat(self):
        self.etat = True if self.etat == False else False
        print(self.etat)
    
    def print_text(self):
        print(self.edit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
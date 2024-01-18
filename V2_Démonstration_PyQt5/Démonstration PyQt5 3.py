import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QCheckBox, QTextEdit

def dialog():
    mbox = QMessageBox()
    mbox.setText("Noté !")
    mbox.setDetailedText("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()
checkbox=None
def check():
    global checkbox
    checkbox = False if checkbox==True else True
    if checkbox==None:
        checkbox= True
    print(checkbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,400)
    w.setWindowTitle("Démonstration")
    
    label = QLabel(w)
    label.setText("Lorem ipsum dolor sit.")
    label.move(100,130)
    label.show()
    
    def print_moi():
        print('Clicked !!')
        
    bouton = QPushButton(w)
    bouton.setText('Click on me')
    bouton.move(110,200)
    bouton.show()
    bouton.clicked.connect(print_moi)
    
    btn = QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)
    
    checkin = QCheckBox(w)
    checkin.setText('Click')
    checkin.move(110,180)
    checkin.show()
    checkin.clicked.connect(check)
    
    w.show()
    sys.exit(app.exec_())
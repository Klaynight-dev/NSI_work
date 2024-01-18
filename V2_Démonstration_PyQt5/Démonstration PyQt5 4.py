import sys
from PyQt5.QtWidgets import QApplication, QWidget , QLabel, QLineEdit, QPushButton
class QLineApp:
 
    def action(self):
        name = self.qlineName.text()
        self.lblResult.setText("Hello : " + name)
        print(name)
 
    def __init__(self , win):
        super().__init__()
        self.win = win
 
    def build(self):
        self.win.setWindowTitle("Example of QLineEdit App")
        self.win.setGeometry(100 , 100 , 500 , 300)
 
        # Label to prompt user to enter his name
        self.lblName = QLabel(self.win)
        self.lblName.setText("Enter Your Name : ")
        self.lblName.setGeometry(50 , 100 , 150 , 30)
        self.lblName.setStyleSheet("font-size: 14px;")
 
        # QLineEdit to enter name
        self.qlineName = QLineEdit (self.win)
        self.qlineName.setGeometry(175 , 100 , 180 , 30)
        self.qlineName.setStyleSheet("font-size: 14px;")
         
        # Label to display result
        self.lblResult = QLabel(self.win)
        self.lblResult.setText(".........................................")
        self.lblResult.setGeometry(175 , 130 , 180 , 30)
        self.lblResult.setStyleSheet("font-size: 14px;")
 
 
        # QPushButton to validate operation
        self.qbtn = QPushButton(self.win)
        self.qbtn.setText("Validate")
        self.qbtn.clicked.connect(self.action)
        self.qbtn.setGeometry(175 , 170 , 180 , 30)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QWidget()
 
    qlineApp = QLineApp(root)
    qlineApp.build()
 
    root.show()
    sys.exit(app.exec_())
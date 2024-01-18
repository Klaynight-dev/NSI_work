import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":

    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("Musketeers")

    btn1 = QPushButton("Athos")
    btn2 = QPushButton("Porthos")
    btn3 = QPushButton("Aramis")

    vb = QVBoxLayout(w)

    vb.addWidget(btn1)
    vb.addWidget(btn2)
    vb.addWidget(btn3)

    w.show()

    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QTimer

class TowerOfHanoi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu tour d'Hanoi")
        self.disks = {
            1: "pink",
            2: "violet",
            3: "indigo",
            4: "blue",
            5: "green",
            6: "yellow",
            7: "orange",
            8: "red"
        }
        self.init_ui()

    def init_ui(self):
        # Create labels for towers
        tower_labels = [QLabel(f"TOUR {i + 1}") for i in range(3)]

        # Create combo box for selecting number of disks
        self.disk_combo = QComboBox()
        self.disk_combo.addItems(["3", "4", "5", "6", "7", "8"])
        self.disk_combo.currentIndexChanged.connect(self.new_game)

        # Create input boxes for move count
        self.min_moves = QLineEdit("255")
        self.min_moves.setReadOnly(True)
        self.your_moves = QLineEdit("0")
        self.your_moves.setReadOnly(True)

        # Create buttons
        self.instruction_btn = QPushButton("Instructions")
        self.instruction_btn.clicked.connect(self.display_instructions)
        self.restart_btn = QPushButton("Recommencer")
        self.restart_btn.clicked.connect(self.new_game)
        self.undo_btn = QPushButton("Annuler")
        self.undo_btn.setDisabled(True)
        self.undo_btn.clicked.connect(self.undo_move)
        self.solve_btn = QPushButton("Solution")
        self.solve_btn.clicked.connect(self.solve)

        # Set up tower and disk layouts
        tower_layouts = [QVBoxLayout() for _ in range(3)]

        disk_layouts = []
        for i in range(8):
            disk = QLabel()
            disk.setStyleSheet(f"background-color: {self.disks[i+1]};")
            disk.setFixedWidth((i + 1) * 20)
            disk.setFixedHeight(19)
            disk.setAlignment(Qt.AlignCenter)
            disk_layouts.append(disk)

        for i in range(3):
            tower_layouts[i].addWidget(QLabel(f"TOUR {i + 1}"))
            for j in reversed(range(8)):
                new_disk = QLabel()
                new_disk.setStyleSheet(disk_layouts[j].styleSheet())
                new_disk.setFixedWidth(disk_layouts[j].width())
                new_disk.setFixedHeight(disk_layouts[j].height())
                new_disk.setAlignment(Qt.AlignCenter)
                tower_layouts[i].addWidget(new_disk)

            tower_layouts[i].addStretch(1)

        # Set up main layout
        main_layout = QVBoxLayout()
        settings_layout = QVBoxLayout()
        settings_layout.addWidget(QLabel("Nombre de disques"))
        settings_layout.addWidget(self.disk_combo)
        settings_layout.addWidget(QLabel("Nombre minimum de déplacements"))
        settings_layout.addWidget(self.min_moves)
        settings_layout.addWidget(QLabel("Votre nombre de déplacements"))
        settings_layout.addWidget(self.your_moves)
        settings_layout.addStretch(1)
        settings_layout.addWidget(self.instruction_btn)
        settings_layout.addWidget(self.restart_btn)
        settings_layout.addWidget(self.undo_btn)
        settings_layout.addWidget(self.solve_btn)

        h_layout = QHBoxLayout()
        for layout in tower_layouts:
            h_layout.addLayout(layout)

        main_layout.addLayout(h_layout)
        main_layout.addLayout(settings_layout)

        self.setLayout(main_layout)
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def new_game(self):
        pass  # Implement new game logic here

    def undo_move(self):
        pass  # Implement undo move logic here

    def solve(self):
        pass  # Implement solve logic here

    def display_instructions(self):
        msg = "Essayer de déplacer tous les disques de la tour 1 à la tour 3.\n"
        msg += "Vous ne pouvez déplacer qu'un disque à la fois.\n"
        msg += "Vous ne pouvez pas mettre un gros disque sur un disque plus petit."
        QMessageBox.information(self, "Instructions", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hanoi_game = TowerOfHanoi()
    sys.exit(app.exec_())
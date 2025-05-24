from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QButtonGroup, QPushButton, QVBoxLayout, QLabel
from functools import partial # Très important pour éviter la repétition du code et bien plus

# Les principaux layouts :
# QVBoxLayout
# QHBoxLayout
# QStackedLayout
# QGridLayout

# Widgets intéressants :
# QLineEdite
# QLabel
# QPushButton

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon application Qt")
        self.setMinimumSize(400, 400)
        self.compteur = 0

        h_layout = QHBoxLayout(self)

        self.label = QLabel("Hello, world !")
        self.label.setPalette(QColor('blue'))
        h_layout.addWidget(self.label)

        self.button = QPushButton("Compter !")
        self.button.clicked.connect(self.button_clicked)
        h_layout.addWidget(self.button)

        self.button2 = QPushButton("Décompter !")
        self.button2.clicked.connect(self.button_discount)
        h_layout.addWidget(self.button2)

    def button_clicked(self):
        self.compteur += 1
        self.label.setText(str(self.compteur))

    def button_discount(self):
        self.compteur -= 1
        self.label.setText(str(self.compteur))


app = QApplication()
main_window = MainWidget()
main_window.show()
app.exec()
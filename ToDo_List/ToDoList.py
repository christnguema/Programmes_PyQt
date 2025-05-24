from PySide6.QtWidgets import QApplication, QWidget

from main import main_window


class MainWin(QWidget):
    def __init__(self):
        super().__init__()

my_app = QApplication()
win = MainWin()
win.show()
my_app.exec()
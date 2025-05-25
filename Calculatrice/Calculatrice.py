from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()




my_win = MainWindow()
calculator_app = QApplication()
my_win.show()
calculator_app.exec()
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")
        self.setFixedSize(400, 400)

        self.main_layout = QVBoxLayout(self)
        self.lw_todos = QListWidget()
        self.le_task_title = QLineEdit()
        self.le_task_title.setPlaceholderText("Tâche à effectuer...")
        self.btn_clear = QPushButton("Tout supprimer")

        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.le_task_title)
        self.main_layout.addWidget(self.btn_clear)

        self.le_task_title.returnPressed.connect(self.add_todo)
        self.btn_clear.clicked.connect(self.lw_todos.clear)
        self.lw_todos.itemDoubleClicked.connect(self.delete_item)

    def add_todo(self):
        self.lw_todos.addItem(self.le_task_title.text())
        self.le_task_title.clear()


    def delete_item(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))

my_app = QApplication()
win = MainWin()


win.show()
my_app.exec()
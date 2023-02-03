from __future__ import annotations
from PyQt5.QtWidgets import *
from functions import *


class NewBase(QMainWindow):
    def __init__(self, Parent) -> None:
        super().__init__()
        self.initUI()
        self.Parent = Parent

    def initUI(self):
        self.setWindowTitle('обнуление')
        self.setGeometry(width // 2 - 100, height//2 - 100, 300, 200)
        self.yes_button = QPushButton("Да", self)
        self.no_button = QPushButton("Нет", self)
        self.yes_button.clicked.connect(self.yes_bc_nb)
        self.no_button.clicked.connect(self.no_bc_nb)
        self.yes_button.move(50, 100)
        self.no_button.move(150, 100)
        self.text1 = QLabel("Вы действительно", self)
        self.text2 = QLabel("хотите уничтожить?", self)
        self.text1.move(100, 10)
        self.text2.move(97, 22)

    def yes_bc_nb(self):
        open('base.txt', 'w').close()
        open('schedule.txt', 'w').close()
        open('tasks.txt', 'w').close()
        self.Parent.__init__()
        self.close()

    def no_bc_nb(self):
        self.Parent.__init__()
        self.close()
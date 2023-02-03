from __future__ import annotations
from PyQt5.QtWidgets import *
from functions import *


class DeleteTask(QMainWindow):
    def __init__(self, Parent0):
        super().__init__()
        self.Parent0 = Parent0
        self.initUI()

    def initUI(self):
        self.setGeometry(width // 2 - 250, height // 2 - 250, 300, 200)
        self.tasks = include_tasks()
        self.setWindowTitle('Настройки')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.combo = QComboBox()
        self.name_sur = []
        for i in range(len(self.tasks)):
            self.name_sur.append(str(self.tasks[i][0] + ' ' + self.tasks[i][3]))
        self.combo.addItems(self.name_sur)
        layout = QVBoxLayout(self.centralWidget)
        layout.addWidget(self.combo)
        self.delete_button = QPushButton("удалить", self)
        self.delete_button.move(55, 150)
        self.delete_button.clicked.connect(self.delete_button_clicked)

        self.r = QLabel("Выберите задачу,", self)
        self.r.move(100, 10)
        self.r1 = QLabel("которую хотите", self)
        self.r1.move(105, 20)
        self.r2 = QLabel("удалить", self)
        self.r2.move(125, 30)

        self.button_back = QPushButton("Назад", self)
        self.button_back.move(155, 150)
        self.button_back.clicked.connect(self.active_button_back)

    def delete_button_clicked(self):
        f = open("tasks.txt", "w+", encoding="utf8")
        for i in range(len(self.tasks)):
            if self.tasks[i][0] + " " + self.tasks[i][3] != self.combo.currentText():
                self.text = self.tasks[i][0] + ", " + self.tasks[i][1] + ", " \
                       + self.tasks[i][2] + ", " + self.tasks[i][3] + '\n'
                f.write(self.text)
        f.close()

        self.Parent0.__init__()
        self.close()

    def active_button_back(self):
        self.Parent0.__init__()
        self.close()
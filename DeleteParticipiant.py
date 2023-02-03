from __future__ import annotations
from PyQt5.QtWidgets import *
from functions import *


class DeleteParticipant(QMainWindow):
    def __init__(self, Parent) -> None:
        QMainWindow.__init__(self)
        self.initUI()
        self.Parent = Parent

    def initUI(self):
        self.setGeometry(width // 2 - 250, height // 2 - 250, 300, 200)
        self.peoples = include_base()
        self.setWindowTitle('Настройки')

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.combo = QComboBox()
        self.text1 = QLabel("Можно удалить:", self)
        self.text1.move(100, 20)
        self.name_sur = []
        for i in range(len(self.peoples)):
            self.name_sur.append(str(self.peoples[i][0] + ' ' + self.peoples[i][1]))
        self.combo.addItems(self.name_sur)
        layout = QVBoxLayout(self.centralWidget)
        layout.addWidget(self.combo)
        self.delete_button = QPushButton("удалить", self)
        self.delete_button.move(55, 150)
        self.delete_button.clicked.connect(self.delete_button_clicked)

        self.button_back = QPushButton("Назад", self)
        self.button_back.move(155, 150)
        self.button_back.clicked.connect(self.back_dp)

    def delete_button_clicked(self):
        f = open("base.txt", "w+", encoding="utf8")
        for i in range(len(self.peoples)):
            if self.peoples[i][0] + " " + self.peoples[i][1] != self.combo.currentText():

                f.write(self.peoples[i][0] + ", " + self.peoples[i][1] + ", "
                        + self.peoples[i][2] + ", " + self.peoples[i][3] + '\n')
        f.close()
        self.tasks = include_tasks()
        f = open("tasks.txt", "w+", encoding="utf8")
        for i in range(len(self.tasks)):

            if self.tasks[i][1] + " " + self.tasks[i][2] != self.combo.currentText():
                self.text = self.tasks[i][0] + ", " + self.tasks[i][1] + ", " \
                            + self.tasks[i][2] + ", " + self.tasks[i][3] + '\n'
                f.write(self.text)

        f.close()

        self.Parent.__init__()
        self.close()

    def back_dp(self):
        self.Parent.__init__()
        self.close()

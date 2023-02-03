from __future__ import annotations
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functions import *


class EditTask3(QMainWindow):
    def __init__(self, new_time, old_time_task, Parent0):
        super().__init__()
        self.new_time = new_time
        self.old_time_task = old_time_task.split()
        self.Parent0 = Parent0
        self.initUI()

    def initUI(self):
        self.setGeometry(width // 2 - 250, height // 2 - 250, 300, 300)
        self.setWindowTitle('Настройки')
        self.ready = []
        self.tasks_ = include_tasks()
        self.iname = []
        self.names = include_base()

        self.currtext = self.new_time
        for i in range(len(self.names)):
            self.iname.append(str(self.names[i][0] + " " + self.names[i][1]))

        self.spi = []
        if len(self.tasks_) != 0:
            for i in range(len(self.tasks_)):
                if self.tasks_[i][0] == self.currtext:
                    self.spi.append(self.tasks_[i][1] + ' ' + self.tasks_[i][2])

            for i in range(len(self.iname)):
                if self.iname[i] not in self.spi:
                    self.ready.append(self.iname[i])
        else:
            self.ready = self.iname

        self.combo = QComboBox(self)
        self.combo.addItems(self.ready)
        self.combo.move(125, 17)

        self.text1 = QLabel("Выбор доступных", self)
        self.text1.move(10, 10)
        self.text11 = QLabel("участников:", self)
        self.text11.move(20, 25)

        self.text2 = QLabel("Название задачи", self)
        self.text2.move(10, 100)
        self.text22 = QLabel("(обязательно):", self)
        self.text22.move(15, 115)

        self.button_choose = QPushButton("Выбрать", self)
        self.button_choose.move(10, 200)
        self.button_choose.clicked.connect(self.onActivated_button_choose)

        self.nameoftask = QLineEdit(self.old_time_task[1], self)
        self.nameoftask.move(125, 107)

        self.error0 = QLabel("Uncorrect", self)
        self.error0.move(300, 100)
        self.error0.setStyleSheet("background-color: red")
        self.error0.setFont(QFont("Comic sans MS", 13))
        self.error0.close()

    def onActivated_button_choose(self):
        if len(self.nameoftask.text()) != 0 and len(self.combo.currentText()) != 0 and ',' not in self.nameoftask.text():
            write_file(str(self.currtext + ", " + ", ".join(self.combo.currentText().split()) + ", " +
                           self.nameoftask.text() + "\n"), "tasks.txt")
            self.Parent0.__init__()
            self.close()
        else:
            self.error0.show()
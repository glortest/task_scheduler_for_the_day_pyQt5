from __future__ import annotations
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functions import *


class EditParticipant2(QMainWindow):
    def __init__(self, name_surname, Parent0, Parent1):
        super().__init__()
        self.name_surname = name_surname.split()
        self.Parent0 = Parent0
        self.Parent1 = Parent1
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Изменение участника')
        self.setGeometry(width // 2 - 250, height // 2 - 250, 500, 300)

        self.base = include_base()

        self.n1 = QLabel("Имя:", self)
        self.n1.move(75, 10)

        self.new_name = QLineEdit(self)
        self.new_name.setText(self.name_surname[0])
        self.new_name.move(100, 12)

        self.name_error = QLabel(self)
        self.name_error.setText("(обязательно)")
        self.name_error.move(205, 13)

        self.surname_error = QLabel(self)
        self.surname_error.setText("(обязательно)")
        self.surname_error.move(205, 43)

        self.n2 = QLabel("Фамилия:", self)
        self.n2.move(50, 40)

        self.new_surname = QLineEdit(self)
        self.new_surname.setText(self.name_surname[1])
        self.new_surname.move(100, 42)

        self.number = 0
        for i in range(len(self.base)):
            if self.base[i][0] == self.name_surname[0] and self.base[i][0] == self.name_surname[1]:
                self.number = i

        self.n3 = QLabel("Телефон:", self)
        self.n3.move(50, 70)

        self.new_phone = QLineEdit(self)
        self.new_phone.setText(self.base[self.number][2])
        self.new_phone.move(100, 72)

        self.n2 = QLabel("Телеграм:", self)
        self.n2.move(47, 100)

        self.new_telega = QLineEdit(self)
        self.new_telega.setText(self.base[self.number][3])
        self.new_telega.move(100, 102)

        self.button_ok = QPushButton("Изменить", self)
        self.button_ok.move(100, 200)
        self.button_ok.clicked.connect(self.buttonOkCLicked)

        self.button_esc = QPushButton("Назад", self)
        self.button_esc.move(200, 200)
        self.button_esc.clicked.connect(self.back_ep2)

        self.error0 = QLabel("Uncorrect", self)
        self.error0.move(300, 100)
        self.error0.setStyleSheet("background-color: red")
        self.error0.setFont(QFont("Comic sans MS", 15))
        self.error0.close()

    def buttonOkCLicked(self):
        if len(self.new_name.text()) != 0 and len(self.new_surname.text()) != 0 and (
            "," not in self.new_name.text() and "," not in self.new_surname.text()
            and "," not in self.new_phone.text() and "," not in self.new_telega.text()
        ):
            f = open("base.txt", "w+", encoding="utf8")

            self.peoples = self.base
            for i in range(len(self.peoples)):
                if self.peoples[i][0] + " " + self.peoples[i][1] != self.name_surname[0] + " " + self.name_surname[1]:
                    self.text = str(self.peoples[i][0] + ", " + self.peoples[i][1] + ", " +
                                    self.peoples[i][2] + ", " + self.peoples[i][3] + '\n')
                else:
                    self.text = str(self.new_name.text() + ", " + self.new_surname.text() + ", " +
                                    self.new_phone.text() + ", " + self.new_telega.text() + "\n")

                f.write(self.text)
            f.close()

            self.tasks = include_tasks()

            f = open("tasks.txt", "w+", encoding="utf8")
            for i in range(len(self.tasks)):
                if self.tasks[i][1] + " " + self.tasks[i][2] != self.name_surname[0] + " " + self.name_surname[1]:
                    self.text = str(self.tasks[i][0] + ", " + self.tasks[i][1] + ", "
                                    + self.tasks[i][2] + ", " + self.tasks[i][3] + '\n')
                else:
                    self.text = str(self.tasks[i][0] + ", " + self.new_name.text()
                                    + ", " + self.new_surname.text() + ", " + self.tasks[i][3] + "\n")
                f.write(self.text)
            f.close()

            self.Parent0.__init__()
            self.close()
        else:
            self.error0.show()


    def back_ep2(self):
        self.Parent1.__init__(self.Parent0)
        self.close()
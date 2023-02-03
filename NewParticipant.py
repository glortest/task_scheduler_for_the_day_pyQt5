from __future__ import annotations
from functions import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class NewParticipant(QWidget):
    def __init__(self, Parent) -> None:
        super().__init__()
        self.Parent = Parent
        self.initUI()
        self.name = ''
        self.surname = ''
        self.phonenumber = ''
        self.telega = ''

    def initUI(self):
        self.setWindowTitle('Добавление нового участника')
        self.setGeometry(width // 2 - 250, height // 2 - 250, 500, 300)

        self.name_t = QLabel(self)
        self.name_t.setText('Имя:')
        self.name_t.move(70, 13)
        self.name_e = QLineEdit(self)
        self.name_e.move(100, 10)

        self.name_error = QLabel(self)
        self.name_error.setText("(обязательно)")
        self.name_error.move(240, 13)

        self.surname_t = QLabel(self)
        self.surname_t.setText('Фамилия:')
        self.surname_t.move(46, 43)
        self.surname_e = QLineEdit(self)
        self.surname_e.move(100, 40)

        self.surname_error = QLabel(self)
        self.surname_error.setText("(обязательно)")
        self.surname_error.move(240, 43)

        self.phonenumber_t = QLabel(self)
        self.phonenumber_t.setText("Номер телефона:")
        self.phonenumber_t.move(6, 73)
        self.phonenumber_e = QLineEdit(self)
        self.phonenumber_e.move(100, 70)

        self.telega_t = QLabel(self)
        self.telega_t.setText("telegram:")
        self.telega_t.move(48, 103)
        self.telega_e = QLineEdit(self)
        self.telega_e.move(100, 100)

        self.button_back = QPushButton("Назад", self)
        self.button_back.move(200, 150)
        self.button_back.clicked.connect(self.back_to_nain)

        self.error0 = QLabel("Uncorrect", self)
        self.error0.move(300, 100)
        self.error0.setStyleSheet("background-color: red")
        self.error0.setFont(QFont("Comic sans MS", 15))
        self.error0.close()

        self.sohranenie = QPushButton(self)
        self.sohranenie.setText("Сохранить")
        self.sohranenie.move(125, 150)
        self.sohranenie.clicked.connect(self.save_newp)

    def save_newp(self):
        if len(self.name_e.text()) != 0 and len(self.surname_e.text()) != 0 and (
            "," not in self.name_e.text() and "," not in self.surname_e.text()
            and "," not in self.phonenumber_e.text() and "," not in self.telega_e.text()
        ) and (
            " " not in self.name_e.text() and " " not in self.surname_e.text()
            and " " not in self.phonenumber_e.text() and " " not in self.telega_e.text()
        ):
            if self.name_e.text() == '':
                self.name = ' '
            else:
                self.name = self.name_e.text()
            if self.surname_e.text() == '':
                self.surname = ' '
            else:
                self.surname = self.surname_e.text()
            if self.phonenumber_e.text() == '':
                self.phonenumber = " "
            else:
                self.phonenumber = self.phonenumber_e.text()
            if self.telega_e.text() == "":
                self.telega = " "
            else:
                self.telega = self.telega_e.text()
            self.close()

            write_file(self.name + ", " + self.surname + ", " + self.phonenumber + ", " + self.telega + "\n",
                       "base.txt")

            self.Parent.__init__()
        else:
            self.error0.show()

    def back_to_nain(self):
        self.Parent.__init__()
        self.close()
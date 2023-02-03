from __future__ import annotations
from EditParticipiant2 import *


class EditParticipant1(QMainWindow):
    def __init__(self, Parent):
        super().__init__()
        self.initUi()
        self.Parent = Parent

    def initUi(self):
        self.setWindowTitle('Изменение участника')
        self.setGeometry(width // 2 - 250, height // 2 - 250, 300, 300)

        self.base = include_base()

        self.text1 = QLabel("Можно изменить:", self)
        self.text1.move(100, 20)

        self.combo = QComboBox(self)
        self.vcombo = []
        for i in range(len(self.base)):
            self.vcombo.append(str(self.base[i][0] + " " + self.base[i][1]))
        self.combo.addItems(self.vcombo)
        self.combo.move(100, 100)

        self.button_ok = QPushButton("Продолжить", self)
        self.button_ok.move(50, 200)
        self.button_ok.clicked.connect(self.resume_ep1)

        self.button_esc = QPushButton("Назад", self)
        self.button_esc.move(150, 200)
        self.button_esc.clicked.connect(self.back_ep1)


    def resume_ep1(self):
        self.s = EditParticipant2(self.combo.currentText(), self.Parent, self)
        self.s.show()
        self.close()

    def back_ep1(self):
        self.Parent.__init__()
        self.close()
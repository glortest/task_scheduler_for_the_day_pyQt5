from NewTask2 import *


class NewTask1(QMainWindow):
    def __init__(self, Parent):
        super().__init__()
        self.initUi()
        self.Parent = Parent

    def initUi(self):
        self.setWindowTitle('Выбор времени выполнения новой задачи')
        self.setGeometry(width // 2 - 250, height // 2 - 250, 500, 300)

        self.combo = QComboBox(self)
        self.text1 = QLabel("Выполнение задачи с:", self)
        self.text1.move(10, 10)
        self.combo.addItems(["9:00", "9:30", "10:00", "10:30",
                             "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
                             "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"])

        self.combo.move(100, 100)
        self.button_choose = QPushButton("Выбрать", self)
        self.button_choose.move(105, 150)
        self.button_choose.clicked.connect(self.onActivatedButtonChoose)

        self.button_back = QPushButton("Назад", self)
        self.button_back.move(205, 150)
        self.button_back.clicked.connect(self.onActivatedButtonBack)

    def onActivatedButtonChoose(self):
        self.s = NewTask2(self.combo.currentText(), self.Parent, self)
        self.s.show()
        self.close()

    def onActivatedButtonBack(self):
        self.Parent.__init__()
        self.close()
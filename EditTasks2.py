from EditTasks3 import *


class EditTask2(QMainWindow):
    def __init__(self, arg, Parent0):
        super().__init__()
        self.initUI()
        self.arg = arg
        self.Parent0 = Parent0

    def initUI(self):
        self.setGeometry(width // 2 - 250, height // 2 - 250, 300, 200)
        self.base = include_base()
        self.setWindowTitle('Настройки')

        self.m = QLabel(self)
        self.m.setText("Выберите")
        self.m.move(125, 10)

        self.m_ = QLabel(self)
        self.m_.setText("время")
        self.m_.move(134, 20)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.combo = QComboBox()
        self.combo.addItems(["9:00", "9:30", "10:00", "10:30",
                                     "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
                                     "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"])
        layout = QVBoxLayout(self.centralWidget)
        layout.addWidget(self.combo)

        self.delete_button = QPushButton("Редактировать", self)
        self.delete_button.move(105, 150)
        self.delete_button.clicked.connect(self.delete_button_clicked)

    def delete_button_clicked(self):
        self.s = EditTask3(self.combo.currentText(), self.arg, self.Parent0)
        self.s.show()
        self.close()
from __future__ import annotations
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from functions import *


class SeeBase(QMainWindow):
    def __init__(self, Parent0) -> None:
        QMainWindow.__init__(self)
        self.Parent0 = Parent0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Настройки')
        self.setGeometry(100, 100, 1300, 900)
        self.base = include_base()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)
        self.initbar()
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(self.base))

        self.table.setHorizontalHeaderLabels(["Имя", "Фамилия", "Телефон", "Телеграм"])

        for i in range(len(self.base)):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(self.base[i][j] + " ")))
            self.table.setItem(i, 4, QTableWidgetItem())

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 100, 100)

    def initbar(self):
        bar = self.menuBar()
        self.file = bar.addMenu("Файл")

        settings = QAction("Вернутся к расписанию", self)
        settings.setShortcut("Ctrl+F7")
        self.file.addAction(settings)

        settings = QAction("Закрыть приложение", self)
        settings.setShortcut("Ctrl+F1")
        self.file.addAction(settings)

        self.file.triggered[QAction].connect(self.initbar_distribution)

    def initbar_distribution(self, q):
        if q.text() == "Вернутся к расписанию":
            self.Parent0.__init__()
            self.close()
        elif q.text() == "Закрыть приложение":
            self.close()
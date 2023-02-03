from __future__ import annotations
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from functions import *


class SeeTasks(QMainWindow):
    def __init__(self, Parent0) -> None:
        QMainWindow.__init__(self)
        self.initUI()
        self.Parent0 = Parent0

    def initUI(self):
        self.setWindowTitle('Настройки')
        self.setGeometry(100, 100, 1300, 900)
        self.tasks = include_tasks()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)
        self.initbar()
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setRowCount(len(self.tasks))

        self.table.setHorizontalHeaderLabels(["Вермя задачи", "Название задачи"])

        for i in range(len(self.tasks)):
            self.table.setItem(i, 0, QTableWidgetItem(str(self.tasks[i][0] + " ")))
        for i in range(len(self.tasks)):
            self.table.setItem(i, 1, QTableWidgetItem(str(self.tasks[i][3] + " ")))

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 100, 100)

    def initbar(self):
        bar = self.menuBar()
        self.file = bar.addMenu("Файл")

        settings = QAction("Вернутся к расписанию", self)
        settings.setShortcut("Ctrl+F6")
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
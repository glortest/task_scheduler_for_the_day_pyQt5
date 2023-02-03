from PyQt5 import QtWidgets
from NewParticipant import *
from EditParticipiant1 import *
from DeleteParticipiant import *
from NewBase import *
from NewTask1 import *
from EditTasks1 import *
from DeleteTask import *
from SeeTasks import *
from SeeBase import *


class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')
        self.showFullScreen()
        self.initbar1()
        self.initbar2()
        self.initbar3()

        self.base = include_base()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(20)
        table.setRowCount(len(self.base))
        grid_layout.addWidget(table, 100, 100)

        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(["ФИО", "9:00", "9:30", "10:00", "10:30",
                                         "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
                                         "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"])

        for i in range(len(self.base)):
            table.setItem(i, 0, QTableWidgetItem(str(self.base[i][0] + " " + self.base[i][1])))
        table.resizeColumnsToContents()

        self.dictionary_tasks = {}
        self.dictionary_times = {"9:00": 1, "9:30": 2, "10:00": 3, "10:30": 4, "11:00": 5, "11:30": 6, "12:00": 7,
                               "12:30": 8, "13:00": 9, "13:30": 10, "14:00": 11, "14:30": 12, "15:00": 13, "15:30": 14,
                               "16:00": 15, "16:30": 16, "17:00": 17, "17:30": 18, "18:00": 19}
        self.tasks = include_tasks()
        for i in range(len(self.tasks)):
            for j in range(len(self.base)):
                if str(self.tasks[i][1] + " " + self.tasks[i][2]) == str(self.base[j][0] + " " + self.base[j][1]):
                    self.dictionary_tasks[str(self.tasks[i][1] + " " + self.tasks[i][2])] = j

        for i in range(len(self.tasks)):
            table.setItem(self.dictionary_tasks[str(self.tasks[i][1] + " " + self.tasks[i][2])],
                          self.dictionary_times[str(self.tasks[i][0])], QTableWidgetItem(str(self.tasks[i][3])))

    def initbar1(self):
        bar = self.menuBar()
        self.file = bar.addMenu("Файл")

        settings = QAction("Новое распределение", self)
        settings.setShortcut("Ctrl+F12")
        self.file.addAction(settings)

        settings = QAction("Закрыть приложение", self)
        settings.setShortcut("Ctrl+F1")
        self.file.addAction(settings)

        self.file.triggered[QAction].connect(self.bar1_buttons)

    def initbar2(self):
        bar = self.menuBar()
        self.file = bar.addMenu("Участник")

        new_participant = QAction("Новый участник", self)
        new_participant.setShortcut("Ctrl+P")
        self.file.addAction(new_participant)

        edit_participant = QAction("Редактироваь участника", self)
        edit_participant.setShortcut("Ctrl+Shift+P")
        self.file.addAction(edit_participant)

        delete_participant = QAction("Удалить участника", self)
        delete_participant.setShortcut("Ctrl+Alt+P")
        self.file.addAction(delete_participant)

        settings = QAction("Посмотреть базу участников", self)
        settings.setShortcut("Ctrl+F7")
        self.file.addAction(settings)

        self.file.triggered[QAction].connect(self.bar2_buttons)

    def initbar3(self):
        bar = self.menuBar()
        self.file = bar.addMenu("Задача")

        new_task = QAction("Новая задача", self)
        new_task.setShortcut("Ctrl+N")
        self.file.addAction(new_task)

        edit_task = QAction("Редактировать задачу", self)
        edit_task.setShortcut("Ctrl+Shift+N")
        self.file.addAction(edit_task)

        delete_task = QAction("Удалить задачу", self)
        delete_task.setShortcut("Ctrl+Alt+N")
        self.file.addAction(delete_task)

        dd = QAction("Посмотреть базу задач", self)
        dd.setShortcut("Ctrl+F6")
        self.file.addAction(dd)

        self.file.triggered[QAction].connect(self.bar3_buttons)

    def bar1_buttons(self, q):
        if q.text() == "Новое распределение":
            self.newall = NewBase(self)
            self.newall.show()
            self.close()
        elif q.text() == "Закрыть приложение":
            self.close()

    def bar2_buttons(self, q):
        if q.text() == "Новый участник":
            self.newp = NewParticipant(self)
            self.newp.show()
            self.close()

        elif q.text() == "Редактироваь участника":
            self.sett1 = EditParticipant1(self)
            self.sett1.show()
            self.close()

        elif q.text() == "Удалить участника":
            self.sett2 = DeleteParticipant(self)
            self.sett2.show()
            self.close()

        elif q.text() == "Посмотреть базу участников":
            self.newall = SeeBase(self)
            self.newall.show()
            self.close()

    def bar3_buttons(self, q):
        if q.text() == "Новая задача":
            self.taskk1 = NewTask1(self)
            self.taskk1.show()
            self.close()
        elif q.text() == "Редактировать задачу":
            self.taskk2 = EditTask1(self)
            self.taskk2.show()
            self.close()
        elif q.text() == "Удалить задачу":
            self.taskk3 = DeleteTask(self)
            self.taskk3.show()
            self.close()
        elif q.text() == "Посмотреть базу задач":
            self.tasw = SeeTasks(self)
            self.tasw.show()
            self.close()

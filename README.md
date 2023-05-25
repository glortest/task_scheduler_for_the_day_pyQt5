# Планировщик задач для команд


##### Основная идея проекта и цель:
Создать ресурс для команды, чтобы их руководитель или сами участники могли планировать свой рабочий день

##### Техническое задание:
- Создать ресурс для планировки задач каждый день
- Подченённые определяются по фамилиии и имени (обязательные поля), а также для удобства можно добавить телефон и телеграмм.
- При вводе задач руководителю должна быть предоставленна возможность указать наименование задачи и фаимилию и имя подчинённого, кому она назначена и время начала её выполнения.
- Для задач должна выполнятся операция по изменению её парамаетров - время и назначенный подчинённый, а также её можно удалить.
- Назначенного подчинённого также можно удалить.
- Руководителю должно быть возможно посмотреть весь план работ подчинённых на день с разбивкой по времени с указанием задачи и ответственного за неё

## Код

#### Используемые библиотеки
```py
from __future__ import annotations
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
```
Но, Кирилл Викторович, не радуйтесь - анотации в коде почти нет. 

#### Вспомогательные функции
##### ```def read_file(name_of_file)```
Функция является вспомогательной и помогает записывать информацию в файлы, в которых сохраняется информация более удобно
```py
f = open(name_of_file, "r", encoding="utf8")
lines = [elem.strip() + "" for elem in f.readlines()]
f.close()
return lines
```

##### ```def write_file(text, name_file)```
Функция, также как и ```read_file``` является вспомогательной и помогает записывать информацию в файлы, в которых хранится информация более удобно.
```py
f = open(name_file, "a+", encoding="utf8")
f.write(text)
f.close()
```

##### ```def include_base()```
Данная функция импортрует из файла ```base.txt``` базу участников. Создана, чтобы в каждом классе не создавать одно и тоже.
```py
participants = read_file("base.txt")
for i in range(len(participants)):
    participants[i] = participants[i].split(", ")
    """Лютый колхоз, потому что сплит работает через то, что сербы заняли 25 июля 1995г."""
    if len(participants[i]) != 4 and participants[i][2] == ' ,':
        participants[i] = [participants[i][0], participants[i][1], " ", " "]
    if len(participants[i]) == 3:
        participants[i] = [participants[i][0], participants[i][1], participants[i][2], " "]
return participants
```

##### ```def include_tasks()```
Данная функция импортрует из файла ```tasks.txt``` базу участников. Создана, также, как и ```include_base``` чтобы в каждом классе не создавать одно и тоже.
```py
tasks = read_file("tasks.txt")
for i in range(len(tasks)):
    tasks[i] = tasks[i].split(", ")
return tasks
```

### Классы
#### ```MainWin(QMainWindow)```

**Функция класса: создание базового окна с таблицей, в которую пользователем в дальнейшем будет заносится план работ**

##### ```def __init__(self)```

```py
def __init__(self) -> None:
    super().__init__()
    self.initUI()
```


##### ```def initUI(self)```
**Создаёт пользовательский интерфейс**
1) Включает полноэкранный режим
2) Подключает верхнее меню
3) Создаёт основную таблицу
4) Даёт пользователю возможности для каких-либо дальнейших действий

```py
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
```

##### ```def initbar1(self)```
**Создание первой плашки верхнего меню**
- Создаёт плашку (кнопку меню "Файл") с кнопками "Новое распределение" и "Закрыть приложение"

```py
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
```
##### ```def initbar2(self)```
**Создание второй плашки верхнего меню**
- Cоздаёт плашку (кнопку меню "Участник") с кнопками "Новый участник", "Редактироваь участника", "Удалить участника" и "Посмотреть базу участников"

```py
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
```

##### ```def initbar3(self)```
**Создание третий плашки верхнего меню**
- Cоздаёт плашку (кнопку меню "Задача") с кнопками "Новая задача", "Редактировать задачу", "Удалить задачу" и "Посмотреть базу задач"

```py
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
```
##### ```def bar1_buttons(self, q)```, ```def bar2_buttons(self, q)```, ```def bar3_buttons(self, q)```
**Подключает к кнопкам плашек, с номером, соответсвующей цифрам после слова *bar* меню функцию соответстующих названию действий**

```py
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

```

#### ```NewParticipant(QWidget)```

**Функция класса: добавление нового участника в бд и в основную таблицу**
В этом классе расскажу только про ```def save_newp(self)``` и про ```def back_to_nain(self)```, потому что я устану для каждого класса всё это поробно расписывать.

##### ```def save_newp(self)```
Функция добавляет нового участника в *base.txt* правильном формате
```py
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
```
**В дальнейшем, в переменных *Parent*, *Parent1*, *Parent0*, а также *self.Parent0*, *self.Parent1*, *self.Parent* во всех классах будет лежать такая штука: в класс, от которого вызывается класс, который нас интересует, назовём матерью, а наш класс - дочерним. Тогда, чтобы не было циклического вызова внутри проекта, и мать не умирала, надо сделать так, чтобы мы не на прямую вызывали в дочери мать. Это, как раз, позволяют создать эти переменные. При инициализации дочери мы помимо нужных нам аргументов передаём ещё и ссылку на мать. Затем, когда дочь уже выполнила свои функции, мы, посредством метода ```self.Parent__init__()``` либо пересоздаём мать уже с именёнными параметрами в дочери, либо же вызываем другой класс, которому одним из аргументов будет являться класс ```Parent``` для передыдущей дочери. Индекс при ```Parent``` показывает насколько мы много прошли цепей мать-дочь от ```MainWin```. То-есть в ```Parent0``` должен лежать экземпляр классa ```MainWin```, а в ```Parent1``` такой класс, которій в названии имеет чиселко 1.

##### ```def back_to_nain(self)```
Функция прикреплет к кнопке ```self.button_back``` действие возврата в основное окно
```py
def back_to_nain(self):
    self.Parent.__init__()
    self.close()
```

#### ```EditParticipant1(QWidget)```, ```EditParticipant2(QWidget)```

**Функция класса: изменение существующего участника и в базе задач, и в основной таблице**

##### ```EditParticipant1(QWidget)``` -> ```def resume_ep1(self):```
Функция прикреплет к кнопке ```self.button_ok``` действие перехода в окно класса ```EditParticipant2(QWidget)```
```py  
def resume_ep1(self):
    self.s = EditParticipant2(self.combo.currentText(), self.Parent, self)
    self.s.show()
    self.close()
```
**В дальнейшем, все функции, в названиях которых есть слово *back*, привязаны к кнопке для возможности перехода в предыдущее окно**

##### ```EditParticipant1(QWidget)``` -> ```def resume_ep1(self):```
Изменяет информацию в *base.txt* и *tasks.txt* согласно данным, введённым пользователем 
```py
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
```
В случае некорректного ввода данных вылезет ошибка, находящаяся в *self.error0*

#### ```class DeleteParticipant(QMainWindow)```
Удаляет информацию об участнике, которого выбрал пользователь, в *base.txt* и *tasks.txt*
###### ```delete_button_clicked(self)```

```py
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
```

#### ```class NewBase(QMainWindow)```
Удаляет всю информацию из файлов *base.txt* и *tasks.txt* об участинках и задачах (проще говоря - делает их пустыми).
###### ```def yes_bc_nb(self)```
(*Сокращение от Yes_ButtonClicked_NewBase*)
```py 
def yes_bc_nb(self):
    open('base.txt', 'w').close()
    open('schedule.txt', 'w').close()
    open('tasks.txt', 'w').close()
    self.Parent.__init__()
    self.close()
```
Здесь действия функции ```back....``` заменяет фунция ```no_bc_nb``` (*Сокращение от No_ButtonClicked_NewBase*)
```py
def no_bc_nb(self):
    self.Parent.__init__()
    self.close()
```

#### ```class NewTask1(QMainWindow)```, ``` NewTask2(QMainWindow)```
**Основная задача этих классов - создать новую задачу**
В ```class NewTask1(QMainWindow)``` пользователь выбирает нужное для исполнения какой-либо задачи время.
В ```class NewTask2(QMainWindow)``` пользователь выбирает исполнителя для данной задачи из всех участников, кто в этот период времени не занят, а так же вводит название задачи.
При инициализации во второй класс мы передаём время, выбранное в первом. Благодаря этому, мы можем сделать так, чтобы всё работало по красоте.

Время исполнения, имя и фамилию, а также название задачи программа записвает в файл *tasks.txt* с помощью функции ```onActivated_button_choose(self)```
```py
def onActivated_button_choose(self):
    if len(self.nameoftask.text()) != 0 and len(self.combo.currentText()) != 0 and ',' not in self.nameoftask.text():
        write_file(str(self.currtext + ", " + ", ".join(self.combo.currentText().split()) + ", " +
                       self.nameoftask.text() + "\n"), "tasks.txt")
        self.Parent0.__init__()
        self.close()
    else:
        self.error0.show()
```
#### ```class EditTask1(QMainWindow)```, ```class EditTask2(QMainWindow)```, ```class EditTask3(QMainWindow)```

Набор данных классов даёт возможность пользователю поменять в задаче время исполнения задачи (```class EditTask2(QMainWindow)```), исполнителя и название (```class EditTask3(QMainWindow)```). В классе ```class EditTask1(QMainWindow)``` пользователь выбирает задачу которую он хочет изменить, посредством выбора времени и названия из выпадающего списка.

###### ```class EditTask1(QMainWindow)``` -> ```def delete_button_clicked(self)```
Удаляет запись о выбранной задаче из *tasks.txt*
```
def delete_button_clicked(self):
    f = open("tasks.txt", "w+", encoding="utf8")
    for i in range(len(self.tasks)):
        if self.tasks[i][0] + " " + self.tasks[i][3] != self.combo.currentText():
            self.text = self.tasks[i][0] + ", " + self.tasks[i][1] + ", " \
                        + self.tasks[i][2] + ", " + self.tasks[i][3] + '\n'
            f.write(self.text)
    f.close()
    self.s = EditTask2(self.combo.currentText(), self.Parent0)
    self.s.show()
    self.close()
```

###### ```class EditTask3(QMainWindow)``` -> ```def onActivated_button_choose(self)```
Добавляет в *tasks.txt* новую запись с данными из старой, удалённой в ```def delete_button_clicked(self)```
```py
def onActivated_button_choose(self):
    if len(self.nameoftask.text()) != 0 and len(self.combo.currentText()) != 0 and ',' not in self.nameoftask.text():
        write_file(str(self.currtext + ", " + ", ".join(self.combo.currentText().split()) + ", " +
                       self.nameoftask.text() + "\n"), "tasks.txt")
        self.Parent0.__init__()
        self.close()
    else:
        self.error0.show()
```
```self.error0.show()``` здесь, как и в каком-то классе выше этот метод позволяет показать пользователю то, что введённые им данные не корректны.


#### ```class DeleteTask(QMainWindow)```
Ничем особо не интересный класс, имеет только одну отличную от других функцию - ```def delete_button_clicked(self)```
Она позволяет удалить из *tasks.txt* выбраннуб пользователем задачу.

```py
def delete_button_clicked(self):
    f = open("tasks.txt", "w+", encoding="utf8")
    for i in range(len(self.tasks)):
        if self.tasks[i][0] + " " + self.tasks[i][3] != self.combo.currentText():
            self.text = self.tasks[i][0] + ", " + self.tasks[i][1] + ", " \
                   + self.tasks[i][2] + ", " + self.tasks[i][3] + '\n'
            f.write(self.text)
    f.close()

    self.Parent0.__init__()
    self.close()
```


#### ```class SeeBase(QMainWindow)```
Данный класс позволяет посмотреть таблицу с данными всех участников, которые были созданы пользователем. 
Также, в нём, как и в ```class MainWin()``` существует верхнее меню, но оно состоит только из одной плашки, кнопки внутри которой дают две возможности - вернуться в ```MainWin``` или закрыть всё.
```py
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
```

#### ```class SeeTasks(QMainWindow)```
Класс позволяет посмотреть таблицу с задачами, которые были созданы пользователем. 
Также, в нём, как и в ```class MainWin()```, а тепереь ещё и ```class SeeBase``` существует верхнее меню, которое состоит только из одной плашки, кнопки внутри которой дают две возможности - вернуться в ```MainWin``` или закрыть всё.
```py
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
```
### Cтарт программы
```py
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    app.exec_()
```
## Для пользователя
##### Горячие клавиши

| Сочетание клавиш | Действие |
| ------ | ------ |
| Ctrl+F1  | Закрыть приложение |
| Ctrl+F12 | Новое распределение|
| Ctrl+P | Новый участник |
| Ctrl+Shift+P | Редактировать участника |
| Ctrl+Alt+P | Удалить участника |
| Ctrl+F7 | Посмотреть базу участников |
| Ctrl+N | Новая задача |
| Ctrl+Shift+N | Редактировать задачу |
| Ctrl+Alt+N | Удалить задачу |
| Ctrl+F6 | Посмотреть базу задач |

##### Какие данные считаются неправильными?
Во входных данных не должно быть
1) Запятых
2) Пустых строк в графах с подписью "обязательно"
3) Большого количества бесполезных пробелов.
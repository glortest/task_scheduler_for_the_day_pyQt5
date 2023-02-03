from __future__ import annotations

width, height = 1920, 1080


def read_file(name_of_file):
    f = open(name_of_file, "r", encoding="utf8")
    lines = [elem.strip() + "" for elem in f.readlines()]
    f.close()
    return lines


def write_file(text, name_file):
    f = open(name_file, "a+", encoding="utf8")
    f.write(text)
    f.close()


def include_base():
    participants = read_file("base.txt")
    for i in range(len(participants)):
        participants[i] = participants[i].split(", ")
        """Лютый колхоз, потому что сплит работает через"""
        if len(participants[i]) != 4 and participants[i][2] == ' ,':
            participants[i] = [participants[i][0], participants[i][1], " ", " "]
        if len(participants[i]) == 3:
            participants[i] = [participants[i][0], participants[i][1], participants[i][2], " "]
    return participants


def include_tasks():
    tasks = read_file("tasks.txt")
    for i in range(len(tasks)):
        tasks[i] = tasks[i].split(", ")
    return tasks

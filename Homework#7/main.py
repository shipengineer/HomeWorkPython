# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах(2 любых формата Например: scv, txt).
# Найти контакт по базе и вывести в консоль, добавить новый контакт и записать его в файл.
import ui_Telephone
import sys
from PyQt5 import QtWidgets


class BookApp(QtWidgets.QMainWindow, ui_Telephone.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_adress()

        # self.button_create.clicked.connect(self.create_record)

    def init_adress(self):
        with open('phonebase.txt', 'r') as data:
            people = data.read()
            people = people.split('\n')
            people = list(map(dicrionary, [x.split(' ') for x in people]))

        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(person["secondName"]))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(person["age"]))
            row = row + 1

    def search(self):
        if self.line_search.text != "":
            self.tableWidget.find(self.line_search.text)
            # def create_record(self):


def dicrionary(elem):
    a1 = []
    a2 = []
    for i in range(0, len(elem)-1):
        if i % 2 == 0:
            a1.append(elem[i])
            a2.append(elem[i+1])
        else:
            continue
    return dict(zip(a1, a2))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BookApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
